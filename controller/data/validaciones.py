import datetime
import unicodedata


# Verificar que el formato de fecha sea el correcto
def validar_fecha(fecha_entrada):
    try:
        fecha = datetime.datetime.strptime(fecha_entrada, "%Y-%m-%d")
        return True
    except:
        return False


# Eliminar espacios y colocar en minúsculas para validar
def normalizar_nombre(nombre):
    if nombre is None:
        return ""
    return "".join(
        c
        for c in unicodedata.normalize("NFD", nombre.lower())
        if unicodedata.category(c) != "Mn"
    ).replace(" x", "")
