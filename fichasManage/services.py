import requests

BASE_URL = "http://127.0.0.1:8080/api/v1/"


def get_fichas():
    url = BASE_URL + "/fichasCampo/"
    r = requests.get(url)
    response = r.json()
    return response


def get_estructuras_geologicas():
    url = BASE_URL + "/estructurasGeologicas/"
    r = requests.get(url)
    response = r.json()
    return response
