from django import forms

from feedback.tasks import send_email_task


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your name')
    email = forms.EmailField(label='Your Email Address')
    message = forms.CharField(label='Your opinion', widget=forms.Textarea(attrs={'rows': 20}))

    def send_email(self):
        send_email_task.delay(name=self.cleaned_data['name'], email=self.cleaned_data['email'], message=self.cleaned_data['message'])
