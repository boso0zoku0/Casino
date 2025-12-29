from fastapi import APIRouter
from payments.crud import router as payment_router

router = APIRouter(prefix="/payments", tags=["Payments"])

router.include_router(payment_router)
