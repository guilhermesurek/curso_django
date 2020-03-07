from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.

def index(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'aula7/index7.html', context=context)