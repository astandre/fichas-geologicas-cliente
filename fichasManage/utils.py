from .constants import *


def build_full_estructuras(data):
    if "EST-diques" in data:
        for dique in data["EST-diques"]:
            for key in CLASE_DIQUE:
                if dique["claseDique"] == key[0]:
                    dique["claseDique"] = key[1]
    if "foliaciones" in data:
        for folicacion in data["foliaciones"]:
            for key in ROCAS_METAFORICAS:
                if folicacion["rocasMetaforicas"] == key[0]:
                    folicacion["rocasMetaforicas"] = key[1]
    return data
