from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome do Aluno')
    cpf = models.CharField(max_length=12,help_text='CPF do Aluno')
