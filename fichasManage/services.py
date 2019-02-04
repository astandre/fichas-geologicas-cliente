import requests

# BASE_URL = "http://127.0.0.1:8080/api/v1/"
BASE_URL = "https://fichas-geologicas-api.herokuapp.com/api/v1/"


def get_fichas():
    url = BASE_URL + "/fichasCampo/"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_ficha(ficha_id):
    url = BASE_URL + "/fichasCampo/" + str(ficha_id)
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_estructuras_geologicas():
    url = BASE_URL + "/estructurasGeologicas/"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_ubicacion_ficha(ficha_id):
    url = BASE_URL + "/fichasCampo/" + str(ficha_id) + "/ubicacionFicha"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_pliegue_ficha(ficha_id):
    url = BASE_URL + "/fichasCampo/" + str(ficha_id) + "/pliegueFicha"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_muestra_ficha(ficha_id):
    url = BASE_URL + "/fichasCampo/" + str(ficha_id) + "/muestraFicha"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_estructura_lineal_ficha(ficha_id):
    url = BASE_URL + "/fichasCampo/" + str(ficha_id) + "/estructuraLinealFicha"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_estructura_planar_ficha(ficha_id):
    url = BASE_URL + "/fichasCampo/" + str(ficha_id) + "/estructuraPlanarFicha"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response


def get_afloramiento_ficha(ficha_id):
    url = BASE_URL + "/fichasCampo/" + str(ficha_id) + "/afloramientoFicha"
    r = requests.get(url, auth=('admin', 'admin'))
    response = r.json()
    return response
