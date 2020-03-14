from aula8.models import Pet
from datetime import datetime

def total_pets(request):
    total = Pet.objects.all().count()
    return {"total_pet": total}

def hora_atual(request):
    hora = datetime.now()
    return {"hora": hora}