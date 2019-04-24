from django import forms
from django.core.mail import send_mail
import logging


logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(label="Tu nombre", max_length=100)
    email = forms.EmailInput()
    phone = forms.NumberInput(max_length=12)
    message = forms.CharField(max_length=600, widget=forms.Textarea)

    def send_mail(self):
        logger.info("Enviando email al servidor cliente")
        message = "De: {0}\{1}".format(
            self.cleaned_data["name"],
            self.cleaned_data["message"]
        )
        send_mail(
            "Site message",
            message,
            "site@jlcontraincendio.com.mx",
            ["customservice@jlvccontraincendio.com"],
            fail_silently=False
        )