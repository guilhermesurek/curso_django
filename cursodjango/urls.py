"""cursodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from aula4.views import index as index4
from aula6.views import index as index6
from aula6.views import editar_contato
from aula7.views import index as index7
from aula7.views import restrita, logout_view, permission_view
from aula9.views import index as index9
from aula10.views import mostra_arquivos_estaticos as index10
from aula11.views import index as index11
from aula13.views import aula13 as index13
from aula13.views import aula13_form

#Aqui criamos uma rota para acessar as imagens dentro do document root
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("aula3.urls")),
    path('aula4', index4),
    path('aula6', index6),
    path('aula6/<int:id>', editar_contato),
    path('login', index7, name='login'),
    path('aula7/restrita', restrita),
    path('aula7/view-carrinho', permission_view),
    path('aula9', index9, name='aula9'),
    path('estatico', index10, name='aula10'),
    path('aula11', index11),
    path('aula13', index13),
    path('aula13-form', aula13_form),
    path('logout', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/',include(debug_toolbar.urls)),
    ] + urlpatterns