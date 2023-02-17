# Boilerplate with Docker Compose for Django, Celery, Redis, and Postgres

Based on article with implemenation details: [Docker compose with Django 4, Celery, Redis and Postgres](https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/)


This boilerplate uses Python 3.11 and Django 4. Create your venv using Python 3.11
#### Create venv
```
python -m venv venv
```
then activate it (depends on system)

#### Create django app
```
cd backend
python manage.py startapp YOURAPP_NAME
```
then add your app in settings.py under backend and urls.py
## Now check if it is workin:

#### Build docker

```
docker-compose build
```

#### Start docker

```
docker-compose up
```

#### Build and run in detached mode

```
docker-compose up --build -d
```

### Stop docker-compose

```
docker-compose down
```
