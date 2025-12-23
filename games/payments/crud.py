import base64
import datetime
import uuid
from enum import Enum
import requests
import var_dump
import yookassa
from pydantic import BaseModel
from fastapi import APIRouter, Request, Response, Query, HTTPException
from sqlalchemy.sql.annotation import Annotated
from yookassa import Payment, Payout
from typing import Literal

from yookassa.domain.response import PaymentListResponse
from yookassa_payout.domain.exceptions.api_error import ApiError
from yookassa_payout.domain.request.deposition_request import DepositionRequest
from yookassa_payout.domain.request.deposition_request_builder import (
    DepositionRequestBuilder,
)
from yookassa_payout.domain.response.deposition_response_builder import (
    DepositionResponseBuilder,
)

router = APIRouter()


class PaymentRequest(BaseModel):
    full_name: str
    email: str
    phone: str
    inn: str

    amount: float
    currency: str = "RUB"
    description: str = "Оплата заказа"
    currency: str = "RUB"


PAYOUT_URL = "https://api.testpay.yookassa.ru/payouts"


def get_auth_header():
    auth_str = f"{'512502'}:{'test_*gYADQfmZQxWie2jrqtWUt0VCgPLktfLgT-jddS3TBeOs'}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    return {"Authorization": f"Basic {b64_auth}"}


@router.post("/create_payment/")
async def create_payment(response: Response):
    res = Payment.create(
        {
            "amount": {"value": 1000, "currency": "RUB"},
            "confirmation": {
                "type": "redirect",
                "return_url": "https://merchant-site.ru/return_url",
            },
            "capture": True,
            "description": "Заказ №72",
            "metadata": {"orderNumber": "72"},
            "receipt": {
                "customer": {
                    "full_name": "Ivanov Ivan Ivanovich",
                    "email": "email@email.ru",
                    "phone": "79211234567",
                    "inn": "6321341814",
                },
                "items": [
                    {
                        "description": "Переносное зарядное устройство Хувей",
                        "quantity": "1.00",
                        "amount": {"value": 1000, "currency": "RUB"},
                        "vat_code": "2",
                        "payment_mode": "full_payment",
                        "payment_subject": "commodity",
                        "country_of_origin_code": "CN",
                        "product_code": "44 4D 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                        "customs_declaration_number": "10714040/140917/0090376",
                        "excise": "20.00",
                        "supplier": {
                            "name": "string",
                            "phone": "string",
                            "inn": "string",
                        },
                    },
                ],
            },
            "payment_order": {
                "type": "utilities",
                "amount": {"value": "100.00", "currency": "RUB"},
                "payment_purpose": "Оплата ЖКУ за июль 2023",
                "recipient": {
                    "name": "ООО УК Жилфонд",
                    "inn": "6321341814",
                    "kpp": "987654321",
                    "bank": {
                        "name": "ПАО Сбербанк",
                        "bic": "044525225",
                        "account": "40702810000000000001",
                        "correspondent_account": "30101810400000000225",
                    },
                },
                "kbk": "18210102000011000110",
                "oktmo": "45382000",
                "payment_period": {"month": 7, "year": 2023},
                "payment_document_id": "123456789012345678",
                "payment_document_number": "123-456",
                "account_number": "1234567890",
                "unified_account_number": "1234567890",
                "service_id": "1234567890123",
            },
            "statements": [
                {
                    "type": "payment_overview",
                    "delivery_method": {"type": "email", "email": "email@email.ru"},
                }
            ],
        }
    )

    var_dump.var_dump(res)


@router.get("/webhook/")
async def get_webhook(request: Request):
    body = await request.json()

    await body.get("event")


@router.post("/makeDeposition")
def func():
    idempotence_key = str(uuid.uuid4())
    payment = Payment.create(
        {
            "amount": {"value": "2.00", "currency": "RUB"},
            "payment_method_data": {"type": "bank_card"},
            "confirmation": {
                "type": "redirect",
                "return_url": "https://www.example.com/return_url",
            },
            "description": "Заказ №72",
        },
        idempotence_key,
    )

    # get confirmation url
    confirmation_url = payment.confirmation.confirmation_url
    return confirmation_url


@router.get("/check/info-payment")
async def check_payment(request: Request):
    payment_id = request.cookies.get("payment_id")
    return Payment.find_one(payment_id=payment_id)


class PaymentMethod(str, Enum):
    yoo_money = "yoo_money"
    bank_card = "bank_card"
    sberbank = "sberbank"
    google_pay = "google_pay"
    apple_pay = "apple_pay"
    bank_transfer = "bank_transfer"
    sbp = "sbp"


@router.get("/check/info-payments", response_model=None)
async def check_payments(
    limit: int,
    methods: PaymentMethod,
):
    cursor = None
    data = {
        "limit": limit,  # Ограничиваем размер выборки
        "payment_method": methods,  # Выбираем только оплату через кошелек
        "created_at_gte": "2020-08-08",  # Созданы начиная с 2020-08-08
        "created_at.lt": "2020-10-20",  # И до 2020-10-20
    }

    while True:
        params = data
        if cursor:
            params["cursor"] = cursor
        try:
            res = Payment.list(params)
            print(" items: " + str(len(res.items)))  # Количество платежей в выборке
            print("cursor: " + str(res.next_cursor))  # Указательна следующую страницу
            var_dump.var_dump(res)

            if not res.next_cursor:
                break
            else:
                cursor = res.next_cursor
        except Exception as e:
            print(" Error: " + str(e))
            break


@router.get("/recipient_payment_verifying")
async def verify_recipient(request: Request):
    idempotence_key = str(uuid.uuid4())
    payout = Payout.create(
        {
            "amount": {"value": "2.00", "currency": "RUB"},
            "payout_destination_data": {
                "type": "sbp",
                "phone": "79000000000",
                "bank_id": "100000000111",
            },
            "description": "Выплата по заказу № 37",
            "metadata": {"order_id": "37"},
        },
        idempotence_key,
    )


@router.post("/recipient_payment")
def create_deposition(data):

    if isinstance(data, dict):
        request = DepositionRequestBuilder.build(data)
    elif isinstance(data, DepositionRequest):
        request = data
    else:
        raise ApiError("Unsupported data format!")

    request.validate()
    return DepositionResponseBuilder.build(request)
