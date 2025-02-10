<div align="center">
  <h1>Анализатор страниц</h1>
</div>

WEB-приложение представляет TODO-лист. Оно добавляет пользователей и каждый пользователь содержит свой список задач.
Каждую задачу можно редактировать, обновлять, добавлять новую и удалять существующие.

#### Авторизацию пользователя

Каждый пользователь проходит регистрацию и авторизуется.

1. Длина URL ссылки не должна превышать 255 символов.
2. URL адрес должен быть формата "https://domen2.domen1".
3. Нельзя добавить ссылки две одинаковые ссылки для проверки.



## Иструкция по установке

1. Для начала необходимо [установить окружение.](https://ru.hexlet.io/courses/python-setup-environment/lessons/venv/theory_unit)
2. Далее [установить uv.](https://docs.astral.sh/uv/#__tabbed_1_1)
3. Установить gunicorn, load_dotenv, bcc.
4. Сгенерировать файл requirement.txt командой `uv pip compile pyproject.toml -o requirements.txt`.
5. Перейти в директорию `python-project-52` и ввести `make build`. Данная команда создаст виртуальное окружение в текущей директории и
соберет пакет, перейдя к команде `make biuld` автоматически. ***!Неоходимо находиться в директории python-project, т.к. в ней есть Makefile. Все make команды будут работать только там.***
6. Чтобы проверить код по линтеру ruff можно ввести `make check`. Для исправления ошибок линтера ввести `make check-fix`.

## Запуск приложения

1. Для запуска приложения на локальной машине введите команду make start.
2. На локальной машине перейдите по ссылке http://127.0.0.1:8000/ .
3. Для запуска приложения на продакшн перейдите по ссылке https://python-project-52-jsnv.onrender.com .

### Hexlet tests and linter status:
[![Actions Status](https://github.com/nic11371/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/nic11371/python-project-52/actions)