This README provides comprehensive instructions for setting up and understanding the Stori Challenge project, tailored for a senior backender software engineer in Python. The project adheres to the MIT standard for open-source software.

## Installation

### Docker Instructions

To set up the project using Docker, follow these steps:

Build the Docker image and run the container:

   ```bash
   docker build -t stori-challenge .
   docker-compose up --force-recreate --build
   ```


**Note**: Execute all processes to ensure correct functionality.


## Endpoints

The project includes the following endpoints:
### POST http://localhost:8000/api/v1/summary_balance/

**Body:**
```json
{
    "email_recipient": "email.recipient@gmail.com"
}
```

**Response:**
```json
{
    "http_message": "SUCCESS",
    "message": "Email sent successfully.",
    "summary_balance": {
        "total_balance": 50.24,
        "month_data": [
            [
                "July",
                3,
                50.5,
                -10.3
            ],
            [
                "August",
                2,
                10.0,
                -25.23
            ]
        ]
    }
}



```
This is  going to send an email with the summary balance from the CSV file.

![image](https://github.com/Jose-Cabrera-FullStack/stori/assets/40355414/098df365-115d-40ec-8083-e37be1cc49d0)


## Amazon S3 Integration

The project includes features for uploading and downloading files to/from Amazon S3. Follow these steps to set it up:

1.- Complete the Amazon S3 credentials in the .env file:
```bash
S3_AWS_REGION=
S3_ACCESS_KEY=
S3_SECRET_KEY=
S3_BUCKET_NAME=
```

Edit the /setup/infrastructure/aws_s3.py file to match your project. Update methods:

put_file_in_s3(**args) (line 24)

download_file_from_s3(**args) (line 42)

## Project Structure
The project's directory structure is organized as follows:

```bash

stori-challenge
├─ .gitignore
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
├─ stori
│  ├─ ...
├─ supervisord.conf
└─ temp
   ├─ ...

```

# Architecture Overview

The core stori Django app encompasses various components:

**adapters.py**: Interacts with external services and APIs.

**admin.py**: Configures Django admin for models.

**apps.py**: Manages app-specific configurations.

**async_tasks.py**: Contains asynchronous task functions.

**domains.py**: Holds domain models and business logic.

**migrations**: Manages Django database migrations.

**models.py**: Defines Django models.

**serializer.py**: Manages serialization and deserialization.

**services.py**: Houses business logic and services.

**tests.py**: Contains tests for the app.

**urls.py**: Manages URL routing for app views.

**views.py**: Defines views and their behavior.

### The setup directory includes setup and configuration files:

**asgi.py, wsgi.py**: Django ASGI and WSGI configurations.

**async_task.py**: Configuration for asynchronous tasks, possibly using Celery.

**infrastructure**: Manages interactions with external infrastructure.

**response_formatter.py**: Used for formatting API responses.

**settings.py**: Django project settings.

**urls.py, views.py**: Main project URL routing and views.

### Additional Files and Directories:

**.arm.requirements**: Requirements specifically for deployment.

**.devcontainer**: Configuration for Visual Studio Code (VSCode) 
development container.

**.gitignore**: Specifies ignored files and directories.

**.vscode**: VSCode configuration files.

**docker-compose.yml**: Docker Compose configuration.

**Dockerfile**: Instructions for building the Docker image.

**gunicorn.conf.py**: Gunicorn (WSGI server) configuration.

**manage.py**: Django management script.

**readme.md**: This file, offering project overview and instructions.

**requirements.txt**: List of Python dependencies.

**start-container.sh**: Script to launch the Docker container.

**supervisord.conf**: Supervisor (process control) configuration.

**temp/.ignore**: File to save S3 files temporarily. For this challenge csv files are saved in this directory.

# License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.
