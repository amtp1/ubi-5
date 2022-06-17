# Ubi-5
## Установка Web-приложения

> Развертывание виртуального окружения

```shell
python -m venv env
```
> Установка зависимостей
```shell
pip install -r requirements.txt
```

> Проведение миграции

```shell
python manage.py makemigrations
python manage.py migrate
```

> Запуск на локальном хосте
```shell
python manage.py runserver
```

## Установка Telegram Bot

> Запуск бота

```shell
python main.py
```