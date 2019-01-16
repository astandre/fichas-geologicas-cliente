from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .services import *
from .utils import *


# Create your views here.

def index(request):
    return render(request, "base.html")


def fichas_campo_todas(request):
    fichas_campo = get_fichas()
    fichas_campo = fichas_campo["_embedded"]["fichasCampo"]
    print(fichas_campo)
    for ficha in fichas_campo:
        ficha["links"] = ficha.pop("_links")
    template = loader.get_template('fichasManage/fichas_todas.html')
    context = {
        'fichas_campo': fichas_campo
    }
    return HttpResponse(template.render(context, request))


def estructuras_geologicas_todas(request):
    estructuras_geologicas = get_estructuras_geologicas()
    estructuras_geologicas = estructuras_geologicas["_embedded"]
    print(estructuras_geologicas)
    estructuras_geologicas = build_full_estructuras(estructuras_geologicas)
    template = loader.get_template('fichasManage/estructuras_todas.html')
    context = {
        'estructuras_geologicas': estructuras_geologicas
    }
    return HttpResponse(template.render(context, request))
