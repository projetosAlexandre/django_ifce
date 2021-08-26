from django import forms
from aluno.models import Aluno

class EstudanteForm(forms.ModelForm):
    model = Aluno
    fields = ['nome','cpf','email','data_nasc']