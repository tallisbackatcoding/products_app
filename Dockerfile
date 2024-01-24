FROM doqteam/gitlab-python-base-image:20231021

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

USER root

COPY products_api /app

WORKDIR /app
