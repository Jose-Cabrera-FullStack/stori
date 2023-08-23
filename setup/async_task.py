from setup.settings import MS_NAME
from setup.infrastructure.celery import app
from setup.infrastructure.aws_logging import put_log


@app.task
def add_cloudwatch_log(log, http_message):
    put_log(message=log, http_message=f'{MS_NAME}/{http_message}')
