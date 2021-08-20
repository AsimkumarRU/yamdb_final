# API сервиса YAMDB
![example workflow](https://github.com/AsimkumarRU/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание

Проект Yamdb_final создан для демонстрации методики DevOps (Development Operations) и идеи Continuous Integration (CI),
суть которых заключается в интеграции и автоматизации следующих процессов:
* синхронизация изменений в коде
* сборка, запуск и тестерование приложения в среде, аналогичной среде боевого сервера
* деплой на сервер после успешного прохождения всех тестов
* уведомление об успешном прохождении всех этапов

Само приложение представляет собой API сервиса отзывов о фильмах, книгах и музыке.
Зарегистрированные пользователи могут оставлять отзывы (Review) на произведения (Title).
Произведения делятся на категории (Category): «Книги», «Фильмы», «Музыка». 
Список категорий может быть расширен администратором. Приложение сделано с помощью Django REST Framework.

Для Continuous Integration в проекте используется облачный сервис GitHub Actions.
Для него описана последовательность команд (workflow), которая будет выполняться после события push в репозиторий.

### Технологии
Docker 20.10.7
Docker-Compose v2.0.0-beta.6
Python 3.8.5
DjangoRestFramework 3.11.0
Postgres 12.4

#### Установка Docker
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop) 
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Установите [Docker Compose](https://docs.docker.com/compose/install/)

### Установка проекта (на примере Linux)

- Создайте папку для проекта YaMDb `mkdir yamdb` и перейдите в нее `cd yamdb`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/AsimkumarRU/yamdb_final .`.
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
```sh
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнер в котором будет развернута БД)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY=... # секретный ключ
DEBUG = True # данную опцию следует добавить для отладки
```
- Запустите docker-compose `sudo docker-compose up -d` 
- Примените миграции `sudo docker-compose exec web python manage.py migrate`
- Соберите статику `sudo docker-compose exec web python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `sudo docker-compose exec web python manage.py createsuperuser --email 'admin@yamdb.com'`

Cписок и подробное описание доступных запросов к приложению можно посмотреть:
* http://178.154.240.93/redoc/

### Автор
Алексей Перерва
