from django.contrib import admin
from django.urls import include, path
from apps.core import views


urlpatterns = [

    #adicionando a view do core
    path('admin/', admin.site.urls),
    #nessa linha to incluindo a url da classe core
    path('', include('core.urls', namespace='core')),
]
