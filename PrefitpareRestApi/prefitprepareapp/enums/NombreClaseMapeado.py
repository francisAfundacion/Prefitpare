from enum import Enum

class NombreClaseMapeado(Enum):
    """
       Enumeración que mapea nombres de clases a valores enteros únicos.
    """
    CATEGORIA = 1
    PERSONATIPO = 2
    INGREDIENTE = 3
    PLATO = 4
    USUARIO = 5

def comprobar_opcion_clase(numNombreClase):
    """
    Verifica si un número entero corresponde a un valor válido dentro de la enumeración NombreClaseMapeado.

    Parámetros:
        numNombreClase (int): Número entero a comprobar.

    Retorna:
        bool: True si el número está en la enumeración, False en caso contrario.
    """
    return numNombreClase in NombreClaseMapeado._value2member_map_

def generar_mensaje_mapeo_objeto(numNombreClase):
    """
    Genera un mensaje de texto con el nombre de la clase mapeada correspondiente al número entero dado.

    Si el número no corresponde a ninguna clase mapeada, devuelve un mensaje de error indicando los valores válidos.

    Parámetros:
        numNombreClase (int): Número entero que representa el nombre de una clase según la enumeración.

    Retorna:
        str: Mensaje con el nombre de la clase en formato título o mensaje de error si el valor es inválido.
    """
    if not comprobar_opcion_clase(numNombreClase):
        return (f"El valor introducido como argumento para generar un mensaje acorde a un número entero "
                    f"que se asocia al nombre de una clase es erróneo.\nLos únicos valores admitidos están"
                    f"comprendidos en el siguiente rango de valores: (1-{len(NombreClaseMapeado)})")
    else:
        valorNombreClaseEnum = NombreClaseMapeado(numNombreClase).name
        return f"{valorNombreClaseEnum.title()}"
