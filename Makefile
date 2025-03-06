install:
	pip install uv
	pip install gunicorn uvicorn
	uv venv
	uv pip install -r requirements.txt

check:
	uv run ruff check .

check-fix:
	uv run ruff check --fix .

start:
	python manage.py runserver

render-start:
	gunicorn task_manager.wsgi

build:
	./build.sh

sync:
	uv sync

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

migrations-user:
	python manage.py makemigrations user

collectstatic:
	python manage.py collectstatic --no-input

translate-compile:
	django-admin compilemessages

translate-makemessages:
	django-admin makemessages -l ru

tests:
	python manage.py test

tests-cov:
	uv run coverage run ./manage.py test
	uv run coverage xml