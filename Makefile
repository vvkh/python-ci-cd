install:
	poetry install

lint:
	poetry run flake8 fizzbuzz

test:
	poetry run pytest --junitxml=junit.xml -v tests

cover:
	poetry run pytest --junitxml=junit.xml -v --cov-report xml --cov-report term --cov=fizzbuzz tests
