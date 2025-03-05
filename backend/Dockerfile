FROM vass5/backend-base:latest

WORKDIR /app

COPY . /app


ENV PYTHONPATH=/app


CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0