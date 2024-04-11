targets: prerequisites
	python3
	virtualenv

install:
	python3 -m venv venv
	. venv/bin/activate && \
	pip install -r requirements.txt
start:
	. venv/bin/activate && \
	uvicorn main:app --reload --reload-exclude 'mongo-data/'
