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

setup:
	docker compose run --rm app make setup

up-exist:
	docker compose up --abort-on-container-exist

compose-start:
	docker compose up

compose-down:
	docker compose down

compose:
	docker compose -f docker-compose.yml up --abort-on-container-exit

compose-test:
	docker compose -f docker-compose.yml up --abort-on-container-exit

compose-build:
	docker compose -f docker-compose.yml build task-manager

compose-build-override:
	docker compose -f docker-compose.override.yml build task-manager

push:
	docker compose -f docker-compose.yml push task-manager

up-development:
	docker run -p 8000:8000 -e NODE_ENV=development nic11371/python-project-52 make start

docker-push:
	docker push nic11371/python-project-52

playbook:
	ansible-playbook -i inventory.yml playbook.yml