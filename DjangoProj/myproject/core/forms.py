from myproject.core.models import Jogo
from django import forms


class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'valor']
