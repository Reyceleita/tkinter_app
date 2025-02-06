import unicodedata

#Función para quitar espacios y colocar en minusculas el nombre
def normalizar_nombre(nombre):
    if nombre in None:
        return ""
    return ''.join(
        c for c in unicodedata.category('NFD', nombre.lower())
        if unicodedata.category(c) != 'Mn'
        ).replace(' x', '')