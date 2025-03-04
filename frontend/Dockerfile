FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt


CMD streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0