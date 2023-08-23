import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

app = Celery('stori')
app.conf.broker_url = 'redis://localhost:6379/0'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {self.request!r}'.format(self=self))


if __name__ == '__main__':
    app.start()
