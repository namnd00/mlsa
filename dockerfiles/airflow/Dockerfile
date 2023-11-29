FROM apache/airflow:latest-python3.8
USER root
RUN apt-get update
USER airflow
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt