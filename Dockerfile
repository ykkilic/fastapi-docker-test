FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY main.py /app/main.py
