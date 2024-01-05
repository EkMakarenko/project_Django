from celery import Celery


celery_app = Celery('project', broker='redis://redis:6379/0')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()
