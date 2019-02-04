from .constants import *


def build_ficha_geologica(ficha):
    if "nomenclaturaUnidadGeologica" in ficha:
        try:
            ficha["nomenclaturaUnidadGeologica"] = UNIDAD_GEOLOGICA[ficha["nomenclaturaUnidadGeologica"]]
        except KeyError:
            print("Key error")
    if "tipoContactoGeo" in ficha:
        try:
            ficha["tipoContactoGeo"] = UNIDAD_GEOLOGICA[ficha["tipoContactoGeo"]]
        except KeyError:
            print("Key error")
    if "limiteContactoGeo" in ficha:
        try:
            ficha["limiteContactoGeo"] = UNIDAD_GEOLOGICA[ficha["limiteContactoGeo"]]
        except KeyError:
            print("Key error")
    if "certezaContactoGeo" in ficha:
        try:
            ficha["certezaContactoGeo"] = UNIDAD_GEOLOGICA[ficha["certezaContactoGeo"]]
        except KeyError:
            print("Key error")
    if "origenRoca" in ficha:
        try:
            ficha["origenRoca"] = UNIDAD_GEOLOGICA[ficha["origenRoca"]]
        except KeyError:
            print("Key error")
    if "estructuraRoca" in ficha:
        try:
            ficha["estructuraRoca"] = UNIDAD_GEOLOGICA[ficha["estructuraRoca"]]
        except KeyError:
            print("Key error")

    if "pliegue" in ficha:
        if "tipo" in ficha["pliegue"]:
            try:
                ficha["pliegue"]["tipo"] = PLIEGUE_TIPO[ficha["pliegue"]["tipo"]]
            except KeyError:
                print("Key error")
        if "posicion" in ficha["pliegue"]:
            try:
                ficha["posicion"] = PLIEGUE_POSICION[ficha["pliegue"]["posicion"]]
            except KeyError:
                print("Key error")
        if "anguloEntreFlancos" in ficha["pliegue"]:
            try:
                ficha["pliegue"]["anguloEntreFlancos"] = PLIEGUE_ANGULO_ENTRE_FLANCOS[
                    ficha["pliegue"]["anguloEntreFlancos"]]
            except KeyError:
                print("Key error")
        if "perfil" in ficha["pliegue"]:
            try:
                ficha["pliegue"]["perfil"] = PLIEGUE_PERFIL[ficha["pliegue"]["perfil"]]
            except KeyError:
                print("Key error")
        if "sistema" in ficha["pliegue"]:
            try:
                ficha["pliegue"]["sistema"] = PLIEGUE_SISTEMA[ficha["pliegue"]["sistema"]]
            except KeyError:
                print("Key error")
    if "eslineal" in ficha:
        if "lineacion" in ficha["eslineal"]:
            try:
                ficha["eslineal"]["lineacion"] = EST_LINEAL_LINEAMIENTO[ficha["eslineal"]["lineacion"]]
            except KeyError:
                print("Key error")
        if "claseEstrLineal" in ficha["eslineal"]:
            try:
                ficha["eslineal"]["claseEstrLineal"] = EST_LINEAL_CLASE[ficha["eslineal"]["claseEstrLineal"]]
            except KeyError:
                print("Key error")
        if "buzamiento" in ficha["eslineal"]:
            try:
                ficha["eslineal"]["buzamiento"] = EST_LINEAL_BUZAMIENTO[ficha["eslineal"]["buzamiento"]]
            except KeyError:
                print("Key error")
        if "asociacion" in ficha["eslineal"]:
            try:
                ficha["eslineal"]["asociacion"] = EST_LINEAL_ASOCIACION[ficha["eslineal"]["asociacion"]]
            except KeyError:
                print("Key error")
        if "formacion" in ficha["eslineal"]:
            try:
                ficha["eslineal"]["formacion"] = EST_LINEAL_FORMACION[ficha["eslineal"]["formacion"]]
            except KeyError:
                print("Key error")
        if "diaclasaClase" in ficha["eslineal"]:
            try:
                ficha["eslineal"]["diaclasaClase"] = EST_LINEAL_DIACLASA_OR_ROCAS[ficha["eslineal"]["diaclasaClase"]]
            except KeyError:
                print("Key error")
    if "esplanar" in ficha:
        if "buzamientoIntensidad" in ficha["esplanar"]:
            try:
                ficha["esplanar"]["buzamientoIntensidad"] = EST_PLANAR_BUZ_INTEN[
                    ficha["esplanar"]["buzamientoIntensidad"]]
            except KeyError:
                print("Key error")
        if "clivaje" in ficha["esplanar"]:
            try:
                ficha["esplanar"]["clivaje"] = EST_PLANAR_CLIVAJE[ficha["esplanar"]["clivaje"]]
            except KeyError:
                print("Key error")
        if "estratificacion" in ficha["esplanar"]:
            try:
                ficha["esplanar"]["estratificacion"] = EST_PLANAR_ESTRAT[ficha["esplanar"]["estratificacion"]]
            except KeyError:
                print("Key error")
        if "fotogeologia" in ficha["esplanar"]:
            try:
                ficha["esplanar"]["fotogeologia"] = EST_PLANAR_FOTO[ficha["esplanar"]["fotogeologia"]]
            except KeyError:
                print("Key error")
        if "zonaDeCizalla" in ficha["esplanar"]:
            try:
                ficha["esplanar"]["zonaDeCizalla"] = EST_PLANAR_ZONA[ficha["esplanar"]["zonaDeCizalla"]]
            except KeyError:
                print("Key error")
        if "rocasMetaforicas" in ficha["esplanar"]:
            try:
                ficha["esplanar"]["rocasMetaforicas"] = EST_LINEAL_DIACLASA_OR_ROCAS[
                    ficha["esplanar"]["rocasMetaforicas"]]
            except KeyError:
                print("Key error")
        if "rocasIgneas" in ficha["esplanar"]:
            try:
                ficha["esplanar"]["rocasIgneas"] = EST_LINEAL_DIACLASA_OR_ROCAS[
                    ficha["esplanar"]["rocasIgneas"]]
            except KeyError:
                print("Key error")
    if "afloramiento" in ficha:
        if "dimension" in ficha["afloramiento"]:
            try:
                ficha["afloramiento"]["dimension"] = AFL_DIMEN[
                    ficha["afloramiento"]["dimension"]]
            except KeyError:
                print("Key error")
        if "origen" in ficha["afloramiento"]:
            try:
                ficha["afloramiento"]["origen"] = AFL_ORIGEN_ROCA[
                    ficha["afloramiento"]["origen"]]
            except KeyError:
                print("Key error")
        if "tipoRoca" in ficha["afloramiento"]:
            try:
                ficha["afloramiento"]["tipoRoca"] = AFL_TIPO_ROCA[
                    ficha["afloramiento"]["tipoRoca"]]
            except KeyError:
                print("Key error")
        if "sitio" in ficha["afloramiento"]:
            try:
                ficha["afloramiento"]["sitio"] = AFL_SITIO[
                    ficha["afloramiento"]["sitio"]]
            except KeyError:
                print("Key error")
    return ficha
