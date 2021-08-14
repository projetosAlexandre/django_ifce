from django.apps import AppConfig


class AlunoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aluno'

class AlunoAppConfig(AppConfig):
    name="django_ifce.apps.aluno"
    verbose_name= "Alunos"