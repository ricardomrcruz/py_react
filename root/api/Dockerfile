FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./.env /app/.env
COPY ./app /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python --version


CMD uvicorn main:app --host 0.0.0.0 --port 80 --reload