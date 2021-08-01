# API сервиса YAMDB
### Описание
Сервис YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории и жанры.
К отзывам могут быть добавлены комментарии других пользователей сервиса.
### Технологии
Docker 20.10.7
Docker-Compose v2.0.0-beta.6
Python 3.8.5
DjangoRestFramework 3.11.0
Postgres 12.4

### Деплой проекта на сервере
- Установите Docker и Docker-Compose
- Скопируйте каталог проекта на свой сервер в домашнюю директорию
- Соберите образы проекта и запустите их на выполнение командой в терминале сервера из каталога проекта:
```
docker-compose up -d --build
``` 
- Выполните следующие команды в терминале сервера из каталога проекта:
```
docker-compose exec web python manage.py makemigrations users titles reviews
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
``` 
- Заполните базу данных проекта тестовыми данными командами в терминале сервера из каталога проекта:
```
docker-compose exec web python manage.py shell  
# выполнить в открывшемся терминале:
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
docker-compose exec web python manage.py loaddata fixtures.json 
```
### Автор
Алексей Перерва

![example workflow](https://github.com/AsimkumarRU/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)