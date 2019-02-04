from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .services import *
from .utils import *


# Create your views here.
# TODO añadir formularios

def index(request):
    return render(request, "base.html")


def fichas_campo_todas(request):
    fichas_campo = get_fichas()
    print(fichas_campo)
    fichas_campo = fichas_campo["_embedded"]["fichasCampo"]
    for ficha in fichas_campo:
        ficha["links"] = ficha.pop("_links")
        ficha = build_ficha_geologica(ficha)
        ficha["id"] = ficha["links"]["fichaCampo"]["href"][
                      ficha["links"]["fichaCampo"]["href"].rfind("/") + 1:len(ficha["links"]["fichaCampo"]["href"])]
    print(fichas_campo)
    template = loader.get_template('fichasManage/fichas_todas.html')

    page = request.GET.get('page', 1)

    paginator = Paginator(fichas_campo, 10)
    try:
        fichas = paginator.page(page)
    except PageNotAnInteger:
        fichas = paginator.page(1)
    except EmptyPage:
        fichas = paginator.page(paginator.num_pages)

    context = {
        'fichas_campo': fichas
    }
    return HttpResponse(template.render(context, request))


def ficha_campo_detail(request, ficha_id):
    ficha_campo = get_ficha(ficha_id)
    ficha_campo["ubicacion"] = get_ubicacion_ficha(ficha_id)
    ficha_campo["pliegue"] = get_pliegue_ficha(ficha_id)
    ficha_campo["muestra"] = get_muestra_ficha(ficha_id)
    ficha_campo["eslineal"] = get_estructura_lineal_ficha(ficha_id)
    ficha_campo["esplanar"] = get_estructura_planar_ficha(ficha_id)
    ficha_campo["afloramiento"] = get_afloramiento_ficha(ficha_id)
    ficha_campo = build_ficha_geologica(ficha_campo)
    # Deleting keys from dict
    del ficha_campo["user"]
    del ficha_campo["_links"]
    del ficha_campo["ubicacion"]["_links"]
    del ficha_campo["pliegue"]["_links"]
    del ficha_campo["muestra"]["_links"]
    del ficha_campo["eslineal"]["_links"]
    del ficha_campo["esplanar"]["_links"]
    del ficha_campo["afloramiento"]["_links"]
    print(ficha_campo)
    template = loader.get_template('fichasManage/ficha_detail.html')
    context = {
        'ficha_campo': ficha_campo
    }
    return HttpResponse(template.render(context, request))

# TODO añadir ficha de descarga en pdf
# ubicacion
# autor
# nombre del registro
