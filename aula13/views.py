from django.shortcuts import render
from .forms import UploadFileForm, UploadFileModelForm
from django.conf import settings
import os
# Create your views here.

def aula13(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES)
            form.save()
    contexto ={
        "form": form
    }
    return render(request, 'aula13/index.html', context=contexto)

def handle_uploaded_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def aula13_form(request):
    form = UploadFileModelForm()
    if request.method == 'POST':
        form = UploadFileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    contexto ={
        "form": form
    }
    return render(request, 'aula13/index.html', context=contexto)

def aula13_session(request):
    ja_viu = request.session.get('ja_viu', False)
    if ja_viu is False:
        request.session["ja_viu"] = True
    context = {
        "ja_viu": ja_viu
    }
    return render(request, "aula13/session.html", context=context) 