from django import forms
from aluno.models import Aluno
from bootstrap_datepicker_plus import DatePickerInput

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','cpf','email','data_nasc','user']
        