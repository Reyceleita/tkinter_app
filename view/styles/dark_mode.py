from tkinter import *


#Fondo principal: #121212 (Negro casi puro, ideal para el fondo)
#Fondo secundario: #414141 (Gris oscuro, para secciones elevadas o tarjetas)
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
                    ("Button.border", {"sticky": "nswe", "border": 1,  "children": [
                        ("Button.padding", {"sticky": "nswe",  "children": [
                            ("Button.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "background": "#414141",  
                    "foreground": "#B0B0B0",
                    "relief": "solid",
                    "bordercolor": "black",
                    "padding": (5,0,5,0),
                    #"font": ["Arial", 24]
                },
                "map": {
                    "background": [("active", "blue")]
                }
            },
            "TEntry": {
                "layout": [
                    ("Entry.field", {"sticky": "nswe", "border": 1,  "children": [
                        ("Entry.padding", {"sticky": "nswe",  "children": [
                            ("Entry.label", {"sticky": "nswe"}),
                            ("Entry.textarea", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "background": "#091032",
                    "foreground": "#03DAC6",
                    "fieldbackground": "#1E1E1E",
                    "insertborderwidth": 10,
                    "relief": "raised",
                    "bordercolor": "black",
                    "padding": (5,3,3,3),
                }
            },
            "TCombobox": {
                "layout": [
                    ("Combobox.border", {"sticky": "nswe", "children":[
                        ("Combobox.padding", {"sticky": "nswe", "children": [
                            ("Combobox.label", {"sticky": "nswe"}),
                            ("Combobx.textarea", {"sticky": "nswe"}),
                            ("Combobox.downarrow", {"side": "right"}),
                        ]})
                    ]})
                ],
                "configure": {
                    "fieldbackground": "#1E1E1E",
                    "background": "#1E1E1E",
                    "arrowcolor": "red",
                    "borderclor": "white",
                    "padding": (5,5,5,5)
                },
                "map": {
                    "bordercolor": [("focus", "green")],
                    "background": [("active", "white")],
                    "arrowcolor": [("active", "blue")]
                }
            }
            
        }
    )
    style.theme_use("Dark_theme")