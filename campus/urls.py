from django.contrib import admin
from django.urls import include, path
from apps.core import views
from apps.aluno import views


urlpatterns = [

    #adicionando a view do core
    path('admin/', admin.site.urls),
    path('estudante/', include('aluno.urls', namespace='aluno')),
    path('', include('core.urls', namespace='core')),
    

]
