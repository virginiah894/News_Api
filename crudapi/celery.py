from __future__ import absolute_import, unicode_literals

from celery import Celery
from datetime import datetime, timedelta

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudapi.settings')

app = Celery('crudapi')

app.config_from_object('django.conf:settings', namespace='notif')

app.conf.beat_schedule = {
    'add-every-24-hours': {
        'task': 'app.tasks.refresh_upvote',
        'schedule': 1.0,
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
