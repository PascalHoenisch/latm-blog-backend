targets: prerequisites
	python3
	virtualenv

install:
	python3 -m venv app/venv
	. app/venv/bin/activate && \
	pip install -r app/requirements.txt
start:
	docker compose up -d
	. app/venv/bin/activate && \
	cd app && uvicorn main:app --reload

docker-start:
	docker compose up -d

docker-down:
	docker compose down
