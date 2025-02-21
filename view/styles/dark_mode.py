from tkinter import *


#Fondo principal: #121212 (Negro casi puro)
#Fondo secundario: #1E1E1E (Gris oscuro)
#Texto primario: #E0E0E0 (Gris claro)
#Texto secundario: #A0A0A0 (Gris medio)
#Botones primarios: #00C896 (Turquesa)
#Botones secundarios: #FF4081 (Rosa neón)
#Resaltados: #FFC400 (Amarillo neón)

#Estilizar interfaz
def dark_theme(style):
    style.theme_create(
        "Dark_theme",
        parent="default",  
        settings={
            ".": {
                "configure": {
                    "background": "#121212", 
                    "foreground": "#B0B0B0"
                }
            },
            "Treeview":{
                "layout": [
                    ("Treeview.treearea", {"sticky": "nswe"})
                ],
                "configure": {
                    "background": "#121212",
                    "fieldbackground": "red",
                }
            },
            "TScrollbar": {
                "Layout": [
                    ("Scrollbar.trough", {"children": [
                        ("Scrollbar.uparrow", {"side": "top", "sticky": "n"}),
                        ("Scrollbar.downarrow", {"side": "bottom", "sticky": "s"}),
                        ("Scrollbar.thumb", {"unit": "1", "sticky": "nswe"})
                    ]})
                ],
                "configure": {
                    "background": "#121212",
                    "troughcolor": "#121212",
                    "bordercolor": "#E0E0E0",
                    "arrowcolor": "#A0A0A0",
                    "troughrelief": "flat",
                    "darkcolor": "#A0A0A0",
                    "relief": "ridge"
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
                    "background": "#00C896",  
                    "foreground": "black",
                    "relief": "raised",
                    "bordercolor": "#005F46",
                    "padding": (5,0,5,0),
                    "borderwidth": 5
                    #"font": ["Arial", 24]
                },
                "map": {
                    "background": [("active", "#119876")]
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
                    "background": "#c7c7c7",
                    "foreground": "black",
                    "fieldbackground": "#c7c7c7",
                    "insertborderwidth": 10,
                    "relief": "raised",
                    "bordercolor": "black",
                    "padding": (5,3,3,3),
                    "insertbackground": "blue",
                },
                map: {
                    "insertbackgroud": [("focus", "white")]
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
                    "padding": (5,5,5,5),
                },
                "map": {
                    "bordercolor": [("focus", "green")],
                    "background": [("active", "white")],
                    "arrowcolor": [("active", "blue")],
                    "fieldbackground": [("readonly", "#1E1E1E")]
                }
            },
            "Advertencia.TLabel":{
                "layout": [
                    ("Label.border", {"sticky": "nswe", "children":[
                        ("Label.padding", {"sticky": "nswe", "children": [
                            ("Label.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "font": ("Arial", 16, "bold"),
                    "foreground": "yellow",
                }
            },
            "Error.TLabel":{
                "layout": [
                    ("Label.border", {"sticky": "nswe", "children":[
                        ("Label.padding", {"sticky": "nswe", "children": [
                            ("Label.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "font": ("Arial", 16, "bold"),
                    "foreground": "Red",
                }
            }
            
        }
    )
    style.theme_use("Dark_theme")