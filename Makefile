.PHONY: all start-consumer start-producer start-notifier start-dashboard run-localstack

start-consumer:
	python3 -m app.consumer

start-producer:
	python3 -m app.producer

start-notifier:
	python3 -m app.notifier

start-dashboard:
	python3 -m app.dashboard.app

run-localstack:
	cd deployment && docker-compose up -d

create-table:
	python3 deployment/setup_dynamodb.py

all: run-localstack create-table start-consumer

