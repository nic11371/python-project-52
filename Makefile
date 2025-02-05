install:
	pip install uv
    pip install gunicorn uvicorn

check:
	uv run ruff check .

check-fix:
	uv run ruff check --fix .

start:
	python manage.py runserver

render-start:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

build:
	./build.sh

sync:
	uv sync

migrate:
	python manage.py makemigrations

collectstatic:
	python manage.py collectstatic --no-input
