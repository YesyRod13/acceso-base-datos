from django.shortcuts import render
from estatico.models import equipo
# Create your views here.

def index(request):
    lista = equipo.objects.order_by('email')
    my_context = {'pinguino' : lista}
    return render(request, 'tarea2/index.html', context= my_context)
