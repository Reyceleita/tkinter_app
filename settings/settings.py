import os
import json


# Crear variable con la ruta de la BD
archivo = r".\settings\config.json"

# Configuración por defecto
default = {"tema": "Light_theme", "background": "#F5F5F5", "foreground": "#333333", "listbg": "#dfdfdf","listfg": "#333333"}


def cargar_config():
    # Cargar configuración del archivo
    if os.path.exists(archivo):
        with open(archivo) as f:
            return json.load(f)
    # Si el archivo esta vacio,se crea uno nuevo
    else:
        guardar_config(default)
        return default


# Guardar el aechivo en la ruta
def guardar_config(config):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
