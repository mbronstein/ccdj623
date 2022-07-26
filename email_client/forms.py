from django import forms
from django.conf import settings
from django.core.mail import send_mail


class EmailForm(forms.Form):
    from = forms.CharField(max_length=120)
    to_name = forms.CharField(max_length=120)
    to_email = forms.EmailField()
    subject = forms.CharField(max_length=70)
    body = forms.CharField(widget=forms.Textarea)
    status = forms.CharField(max_length=70)
    # attachment = forms.FileField(?)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
