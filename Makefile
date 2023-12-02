SHELL:=/bin/bash

DEBUG:=True
IMAGE_NAME:=serving
IMAGE_TAG:=latest

env_up:
	source ./.env && docker-compose up --build -d

env_down:
	docker-compose down

env_restart:
	docker-compose restart

serving_dev_up:
	gunicorn src.serving.api:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --reload

serving_prod_up:
	docker build -f dockerfiles/serving/Dockerfile -t "${IMAGE_NAME}:${IMAGE_TAG}" .
	docker-compose -f dockerfiles/serving/docker-compose.yml up -d
