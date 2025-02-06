from tkinter import *


#Fondo principal: #121212 (Negro casi puro, ideal para el fondo)
#Fondo secundario: #1E1E1E (Gris oscuro, para secciones elevadas o tarjetas)
#Texto principal: #E0E0E0 (Gris muy claro, para buena legibilidad)
#Texto secundario: #B0B0B0 (Gris más tenue para información menos destacada)
#Acento 1: #BB86FC (Morado vibrante, estilo Material Design)
#Acento 2: #03DAC6 (Cian brillante, ideal para destacar elementos)
#Error/Advertencia: #CF6679 (Rojo tenue pero llamativo)


def dark_theme(style):
    style.theme_create(
        "Dark_theme",
        parent="clam",  
        settings={
            ".": {
                "configure": {
                    "background": "#121212", 
                    "foreground": "#B0B0B0"
                }
            },
            "TButton": {
                "layout": [
                    ("Button.border", {"sticky": "nswe", "border": 10, "children": [
                        ("Button.padding", {"sticky": "nswe", "children": [
                            ("Button.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "background": "lightblue",  
                    "foreground": "darkblue",
                    "relief": "solid"
                    #"font": ["Arial", 24]
                },
                "map": {
                    "background": [("active", "blue")]
                }
            },
            "TEntry": {
                "layout": [
                    ("Entry.field", {"sticky": "nswe", "border": 100,  "children": [
                        ("Entry.padding", {"sticky": "nswe",  "children": [
                            ("Entry.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "background": "#091032",
                    "foreground": "#03DAC6",
                    "fieldbackground": "#1E1E1E",
                    "insertborderwidth": 10,
                    "relief": "raised"
                }
            },
            "TCombobox": {
                "layout": [
                    ("Combobox.border", {"sticky": "nswe", "border": 50, "children":[
                        ("Combobox.padding", {"sticky": "nswe", "children": [
                            ("Combobox.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "fieldbackground": "#1E1E1E",
                    "background": "#1E1E1E",
                    
                }
            }
            
        }
    )
    style.theme_use("Dark_theme")