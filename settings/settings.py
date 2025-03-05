import os
import json 


#Crear variable con la ruta de la DB
archivo = r'.\settings\config.json'

def cargar_config():
    #Cargar configuración del archivo
    if os.path.exists(archivo):
        with open(archivo) as f:
            return json.load(f)
    #Si el archivo esta vacio,se crea uno nuevo
    else:
        guardar_config(archivo)

#Guardar el aechivo en la ruta
def guardar_config(config):
    with open(archivo, "w", encoding='utf-8') as f:
        json.dump(config, f, indent=4)

#Aplicar el estilo pasado cómo parámetro
def aplicar_tema(style, main):
    tema = cargar_config()
    bg = tema['background']
    fg = tema['foreground']
    tema = tema['tema']
    style.theme_use(tema)
    
    main.option_add("*background", bg)
    main.option_add("*foreground", fg)