FROM python:3.13.2

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app


RUN pip install uv

COPY ../pyproject.toml uv.lock ./
COPY . .

CMD ["uv", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]


