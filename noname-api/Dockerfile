FROM python:latest

RUN apt update
RUN apt upgrade -y

RUN pip install flask pymongo

RUN apt install -y wget
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
CMD dockerize -wait tcp://database-mongo:27017
CMD dockerize -wait tcp://redis:6379

ENV PYTHONPATH=/opt
ENV FLASK_APP=api:server
CMD flask run -h 0.0.0.0
