from django import forms
from .models import Cao


class CaoForm(forms.ModelForm):
    class Meta:
        model = Cao
        fields = ['nome', 'raca', 'idade']