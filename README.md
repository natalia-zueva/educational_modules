# Проект "Образовательные модули"

Данный проект представляет собой контейнеризированную версию Django-приложения “Образовательные модули”.

## Технологии

- Python
- Django (Django REST framework)
- PostgresQL (БД для хранения данных)
- Docker

## Возможности

- Регистрация и авторизация пользователей
- Зарегистрированный пользователь может создавать, изменять и удалять образовательные модули
- Список модулей и просмотр каждого модуля доступны для всех, в том числе и для незарегистрированных пользователей
- Вывод списка модулей производится по 10 штук на странице


## Запуск проекта:

1. Установите Docker и docker-compose на вашем компьютере.
2. Склонируйте репозиторий https://github.com/natalia-zueva/educational_modules на свой компьютер.
3. Перейдите в корневую директорию проекта.
4. Запустите приложение с помощью команды:
* docker-compose build --up

## Документация API:

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/swagger/