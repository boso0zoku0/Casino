FROM python:3.13.2

WORKDIR /app

# Устанавливаем зависимости
COPY games/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY games .

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]