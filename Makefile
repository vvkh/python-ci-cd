install:
	poetry install

lint:
	poetry run flake8 fizzbuzz

test:
	poetry run pytest -v tests

cover:
	poetry run pytest -v --cov-report xml --cov-report term --cov=fizzbuzz tests
