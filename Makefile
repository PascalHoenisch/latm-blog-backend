targets: prerequisites
	python3
	virtualenv

install:
	python3 -m venv app/venv
	. app/venv/bin/activate && \
	pip install -r app/requirements.txt
start:
	. app/venv/bin/activate && \
	cd app && uvicorn main:app --reload
