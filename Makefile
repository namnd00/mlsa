SHELL:=/bin/bash

DEBUG:=True

env_up:
	source ./.env && docker-compose up --build -d

env_down:
	docker-compose down

env_restart:
	docker-compose restart

serving_up:
	gunicorn src.serving.api:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --reload
