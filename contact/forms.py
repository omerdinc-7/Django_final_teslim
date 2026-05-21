from django import forms
from django.conf import settings
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)
    last_name = forms.CharField(max_length=254, required=True)
    email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=254, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_email(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            last_name = self.cleaned_data['last_name']

            # GÜNCELLEME 1: Çakışmayı önlemek için 'email' yerine 'user_email' dedik
            user_email = self.cleaned_data['email']

            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']

            # GÜNCELLEME 2: 'messsage' yazım hatası düzeltildi ve f-string ile modernleştirildi
            message_context = (
                f"Message received.\n\n"
                f"Name: {name} {last_name}\n"
                f"Email: {user_email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message}"
            )

            # GÜNCELLEME 3: Obje adı formdaki veriyle çakışmasın diye 'msg' yapıldı
            msg = EmailMessage(
                subject=f"Site Contact: {subject}",
                body=message_context,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[user_email],
            )
            msg.send()