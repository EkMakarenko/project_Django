from django.contrib.auth.models import UserManager as BaseUserManager

from authentication.tasks import send_activation_email_task


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        response = super().create_user(username, email, password, **extra_fields)
        send_activation_email_task.delay(email=email, message='Activate')

        return response
