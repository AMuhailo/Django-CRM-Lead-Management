from .base import *

DEBUG = False

ADMINS = [
    ("Muhailo I", 'amuhailo25@gmail.com')
]

ALLOWED_HOSTS = ['127.0.0.1','localhost','loadsystem.com', 'www.loadsystem.com', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST':'db',
        'PORT':5432,
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BROCKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60