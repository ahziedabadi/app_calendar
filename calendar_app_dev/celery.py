from __future__ import absolute_import

import os

from celery import Celery
from calendar_app_dev.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calendar_app_dev.settings.development")

app = Celery("calendar_app_dev")

app.config_from_object("calendar_app_dev.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
