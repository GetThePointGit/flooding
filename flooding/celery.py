from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flooding.developmentsettings')

from django.conf import settings  # noqa

app = Celery('proj')

print(" SETTITITITI %s" % settings.DATABASES)  
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    BROKER_URL='amqp://flooding:frmq60A@119-rmq-d1.external-nens.local:5672/flooding',
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler'
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
