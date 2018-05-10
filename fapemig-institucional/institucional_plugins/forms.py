from django import forms
from .models import PessoaModel
from django_summernote.widgets import SummernoteWidget

class PessoaForm(forms.ModelForm):
    class Meta:
        model = PessoaModel
        fields = '__all__'
        widgets = {
            'info': SummernoteWidget(),
        }