FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY course4-app /course4-app
WORKDIR /course4-app
EXPOSE 8000

RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password course4-user


USER course4-user
