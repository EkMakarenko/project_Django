from time import sleep

from django import forms
from django.conf import settings
from django.core.mail import send_mail

from feedback.tasks import send_email_task


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your name')
    email = forms.EmailField(label='Your Email Address')
    message = forms.CharField(label='Your opinion', widget=forms.Textarea(attrs={'rows': 20}))

    def send_email(self):
        # sleep (20)
        # send_mail(
        #     subject='Your feedback',
        #     message=f'{self.cleaned_data["message"]}\n\n Thank you ;)',
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[self.cleaned_data['email']],
        #     fail_silently=False
        #
        # )
        send_email_task.delay(name=self.cleaned_data['name'], email=self.cleaned_data['email'], message=self.cleaned_data['message'])
