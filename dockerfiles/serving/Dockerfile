FROM python:3.8-slim-buster
RUN apt-get update && \
    apt-get install gcc python3-dev --yes && \
    apt-get install libevent-dev --yes
COPY ./dockerfiles/serving/requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY ./src /app/src
WORKDIR /app