FROM vass5/backend-base:latest

WORKDIR /app

COPY . /app


ENV PYTHONPATH=/app

RUN  pip install giskard && \
    pip install "giskard[llm]" && \
    pip install litellm && \
    pip install openai && \
     pip install sentence-transformers


CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0