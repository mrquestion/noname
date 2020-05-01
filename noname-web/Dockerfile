FROM python:latest

RUN apt update
RUN apt upgrade -y

RUN pip install flask requests

RUN apt install -y wget
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
CMD dockerize -wait http://api:5000

ENV PYTHONPATH=/opt
ENV FLASK_APP=web:server
CMD flask run -h 0.0.0.0
