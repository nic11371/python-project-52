install:
	pip install uv

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

migrate:
	python manage.py makemigrations

collectstatic:
	python manage.py collectstatic --no-input