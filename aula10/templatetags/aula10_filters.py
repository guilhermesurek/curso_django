from django import template
from django.template.defaultfilters import stringfilter
from aula8.models import Pet

register = template.Library()

@register.filter
@stringfilter
def swap(value):
    return value.swapcase()

@register.filter
@stringfilter
def bold(value):
    return f'<b>{value}</b>'

@register.simple_tag
def pega_pet_pelo_nome(pet_name):
    pet = Pet.objects.get(nome=pet_name)
    return pet

@register.filter
def identifica_usuario(user):
    if user.is_authenticated:
        msg = f"<h1>Seja Bem Vindo {user}!</h1>"
    else:
        msg = "<h1>Você não é Bem Vindo!</h1>"
    return msg