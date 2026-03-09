FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src ./src
COPY frontend ./frontend

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8888"]
