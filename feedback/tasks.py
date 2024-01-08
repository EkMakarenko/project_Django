from time import sleep

from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@shared_task
def send_email_task(email, message):
    sleep(20)
    send_mail(
        subject='Your opinion',
        message=f'{message}\n\nThank You ;)',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False
    )
    logger.info('File sent successfully.')
