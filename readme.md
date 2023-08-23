# Microservice Base Project DRF Based
## Instructions to use
### Installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ./manage.py migrate
```
### Run Project (venv activated)
```
python manage.py runserver
```

### Add Django App (venv activated)
```
python manage.py startapp stori
```

## Docker instructions
### Run container
```
docker build -t django-base-ms .
docker-compose up --force-recreate --build
```

##

## Celery

**NOTE: execute all proccess to correctly work**

### 1 - Execute Worker (Engine):
```
celery -A setup worker -l info -P eventlet
```

### 2 - Execute Beat (Scheduled Tasks):
```
celery -A setup beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

### 3 - Execute Frontend (Engine):
```
celery -A setup flower
```

## Amazon S3 implementated

### This template contains files for upload and download files for Amazon S3

**NOTE: You need create a new Bucket for put the files if you need**
**NOTE 2: You need edit /setup/infastrucrure/aws_s3.py file for adapt to project**

1. Complete credentials for Amazon S3 in `.env` file:
```
S3_AWS_REGION=
S3_ACCESS_KEY=
S3_SECRET_KEY=
S3_BUCKET_NAME=
```
2. Edit `/setup/infastrucrure/aws_s3.py` file for adapt to project. Methods to edit:
```
def put_file_in_s3(**args) -> line 24
def download_file_from_s3(**args) -> line 42
```

## Project Structure
The project is organized into several directories and files:

```
django-base-ms
├─ .arm.requirements
├─ .devcontainer
│  ├─ devcontainer.json
│  └─ docker-compose.yml
├─ .gitignore
├─ .vscode
│  └─ launch.json
├─ stori
│  ├─ adapters.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ async_tasks.py
│  ├─ domains.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializer.py
│  ├─ services.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
├─ gunicorn.conf.py
├─ manage.py
├─ readme.md
├─ requirements.txt
├─ setup
│  ├─ asgi.py
│  ├─ async_task.py
│  ├─ infrastructure
│  │  ├─ aws_logging.py
│  │  ├─ aws_s3.py
│  │  └─ celery.py
│  ├─ response_formatter.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ start-container.sh
├─ supervisord.conf
└─ temp
   └─ .ignore

```

## Architecture Overview

- `stori`: The core Django app containing the application-specific code.
  - `adapters.py`: Adapter classes or functions interfacing with external services, APIs or frameworks.
  - `admin.py`: Django admin configuration for the app's models.
  - `apps.py`: Configuration for the app itself.
  - `async_tasks.py`: Functions for handling asynchronous tasks.
  - `domains.py`: Domain models and business logic.
  - `migrations`: Django database migrations.
  - `models.py`: Django model definitions.
  - `serializer.py`: Serializers for data serialization and deserialization.
  - `services.py`: Business logic and application services.
  - `tests.py`: Tests for the app.
  - `urls.py`: URL routing for the app's views.
  - `views.py`: Defines views and their behavior.
#
- `setup`: Contains setup and configuration files for the project.
  - `asgi.py`, `wsgi.py`: Django ASGI and WSGI configurations for serving the application.
  - `async_task.py`: Configuration for handling asynchronous tasks (possibly using Celery).
  - `infrastructure`: Files related to interacting with external infrastructure (AWS in this case).
  - `response_formatter.py`: Used for formatting API responses.
  - `settings.py`: Django settings for the project.
  - `urls.py`: URL routing for the main project's views.
  - `views.py`: Main views and their behavior.

#
- **Other Files and Directories**:
  - `.arm.requirements`: requirements only for deploying.
  - `.devcontainer`: Configuration for Visual Studio Code (VSCode) development container.
  - `.gitignore`: Specifies files and directories ignored by version control (Git).
  - `.vscode`: Configuration files for Visual Studio Code (VSCode).
  - `docker-compose.yml`: Configuration for Docker Compose.
  - `Dockerfile`: Instructions for building a Docker image of the project.
  - `gunicorn.conf.py`: Gunicorn (Python WSGI HTTP server) configuration.
  - `manage.py`: Django management script for various commands.
  - `readme.md`: This file, providing an overview and instructions for the project.
  - `requirements.txt`: List of Python dependencies required by the project.
  - `start-container.sh`: Script to start the Docker container of the application.
  - `supervisord.conf`: Configuration file for Supervisor, a process control system.
  - `temp/.ignore`: A file to save S3 files and removed.
