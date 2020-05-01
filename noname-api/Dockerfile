FROM python:latest

RUN apt update
RUN apt upgrade -y

ENV PYTHONPATH=/opt
ENV FLASK_APP=api:server
CMD flask run -h 0.0.0.0
