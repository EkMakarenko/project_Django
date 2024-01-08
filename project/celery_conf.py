from celery import Celery
from celery.schedules import crontab

celery_app = Celery('project', broker='redis://redis:6379/0')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'delete_deleted_apartments': {
        'task': 'hotel_rest.tasks.delete_deleted_apartments',
        'schedule': crontab(day_of_month='1', hour='0', minute='0'),
    },

    'delete_deleted_hotels': {
        'task': 'hotel_rest.tasks.delete_deleted_hotels',
        # 'schedule': crontab('0 0 * */6 *'),
        'schedule': crontab('*/2 * * * *'),
    },

    'print_message': {
        'task': 'hotel_rest.tasks.print_message',
        'schedule': crontab('*/2 * * * *'),
    }
}
