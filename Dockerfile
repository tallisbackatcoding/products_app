FROM python:3.9-alpine

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

USER root

COPY products_api /app

WORKDIR /app
