FROM python:3.11

WORKDIR /app

COPY . /app

RUN apt update && apt install -y sqlite3

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

ENV PYTHONPATH=/app


CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0