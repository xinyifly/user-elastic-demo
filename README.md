# user_elastic

## Prerequirements

- MySQL
- RabbitMQ
- Elasticsearch

## Get Started

### Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Copy example environments

```bash
cp .env.example .env
```

### Create database

```sql
CREATE DATABASE user_elastic DEFAULT CHARACTER SET utf8;
```

### Create elastic index

```bash
curl -X PUT 127.0.0.1:9200/users
```

### Migrate database

```bash
./manage.py migrate
```

### Start celery worker

```bash
celery -A user_elastic worker -l info
```

### Start server

```bash
./manage.py runserver
```

### Run tests

```bash
./manage.py test
```

## Pagination

- Use `limit` , `offset` pagination style
- Use `X-Total-Count` header indicator
