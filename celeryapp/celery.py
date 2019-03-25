from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celeryapp.settings')


app = Celery('celeryapp',
             broker='amqp://',
             backend='amqp://',
             include=['celeryapp.tasks'])

app.conf.update(
    result_expires=3600,
)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()



if __name__ == '__main__':
    app.start()