from django.forms import ModelForm
from .models import Comentario
import requests

class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data

        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data = {
                'secret': 'your secret site key',
                'response': recaptcha_response
            }
        )
        recaptcha_request = recaptcha_request.json()

        if not recaptcha_request.get('success'):
            self.add_error(
                'comentario',
                'ROBÔS NÃO SÃO PERMITIDOS NESSE LOCAL humph'
            )

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
