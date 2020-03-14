from django.shortcuts import render

# Create your views here.

def mostra_arquivos_estaticos(request):
    return render(request, "aula10/aula10.html", {'titulo':'Aula 10'})