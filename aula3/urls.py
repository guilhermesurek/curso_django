from django.urls import path
from . import views


app_name = "aula3"

'''
    Aqui criamos uma rota para acessar as imagens dentro do document root
se colocar a barra o mesmo chama o diretorio passando o mesmo, sem ele é passado
que o mesmo faz referencia ao init 
'''

urlpatterns = [
    path('', views.index),
    path('cookie', views.setCookie),
    path('uol', views.redirect),
    path('<int:code>', views.show_code),
    path('cat/<int:code>', views.catting),
    path('get/', views.show_get_status),
    path('post/', views.show_post_values),
]
