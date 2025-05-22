from enum import Enum

class NombreClaseMapeado(Enum):
    CATEGORIA = 1
    PERSONATIPO = 2
    INGREDIENTE = 3
    PLATO = 4
    USUARIO = 5

def comprobar_opcion_clase(numNombreClase):
        return numNombreClase in NombreClaseMapeado._value2member_map_

def generar_mensaje_mapeo_objeto(numNombreClase):
        if not comprobar_opcion_clase(numNombreClase):
            return (f"El valor introducido como argumento para generar un mensaje acorde a un número entero "
                    f"que se asocia al nombre de una clase es erróneo.\nLos únicos valores admitidos están"
                    f"comprendidos en el siguiente rango de valores: (1-{len(NombreClaseMapeado)})")
        else:
            valorNombreClaseEnum = NombreClaseMapeado(numNombreClase).name
            return f"{valorNombreClaseEnum.title()}"
