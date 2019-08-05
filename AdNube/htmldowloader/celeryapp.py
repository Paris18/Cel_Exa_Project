import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'htmldowloader.settings')

celery_app = Celery('htmldowloader')
celery_app.conf.broker_url = 'redis://localhost:6379/0'
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)