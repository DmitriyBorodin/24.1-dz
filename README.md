### Learning Management System API
Этот проект разработан с использованием Django REST Framework (DRF) и предназначен для размещения учебных материалов. В рамках проекта пользователи могут выбирать и оплачивать курсы, а также получают уведомления по электронной почте об обновлениях курсов, на которые они подписаны. Реализована авторизация с помощью JWT-токена, а также предусмотрена документация API с использованием Swagger. Проект использует виртуальное окружение Poetry для управления зависимостями.

## Установка и запуск проекта
Клонирование репозитория
```
git clone git@github.com:DmitriyBorodin/24.1-dz.git
```

Создание и активация виртуального окружения Убедитесь, что у вас установлен Poetry.
Затем выполните:
```
poetry install
```

## Настройка окружения

Создайте файл .env в корне проекта и добавьте необходимые переменные окружения, такие как параметры
для базы данных и секретные ключи.
Запуск Docker-контейнеров. Убедитесь, что у вас установлен Docker и Docker Compose. Затем выполните:

``` bash
docker-compose up --build
```
Это создаст и запустит контейнеры для приложения, базы данных и Redis.

## Документация
 - GET /swagger/: Документация в формате Swagger UI.
 - GET /redoc/: Документация в формате ReDoc.
## Используемые технологии:
 - Python 3.12
 - Django 4.2.2
 - PostgreSQL
 - Django REST Framework
 - Celery
 - Redis
 - Docker
 - Docker Compose
