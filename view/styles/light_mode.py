def light_theme(style):
    style.theme_create(
        "Light_theme",
        parent="default",  
        settings={
            ".": {
                "configure": {
                    "background": "#F5F5F5", 
                    "foreground": "#333333"
                }
            },
            "Treeview":{
                "configure": {
                    "background": "#FFFFFF",
                    "fieldbackground": "#DDDDDD",
                }
            },
            "Treeview.Heading":{
                "configure": {
                    "background": "#e5e5e5",
                }
            },
            "TButton": {
                "configure": {
                    "background": "#007BFF",
                    "foreground": "white",
                    "relief": "raised",
                    "padding": (5,0,5,0),
                    "borderwidth": 5,
                    "bordercolor": "#0056b3"
                },
                "map": {
                    "background": [("active", "#0056b3")]
                }
            },
            "TScrollbar": {
                "layout": [
                    ("Scrollbar.trough", {"children": [
                        ("Scrollbar.uparrow", {"side": "top", "sticky": "n"}),
                        ("Scrollbar.downarrow", {"side": "bottom", "sticky": "s"}),
                        ("Scrollbar.thumb", {"unit": "1", "sticky": "nswe"})
                    ]})
                ],
                "configure": {
                    "background": "#F5F5F5",
                    "troughcolor": "#F5F5F5",
                    "bordercolor": "#E0E0E0",
                    "arrowcolor": "#A0A0A0",
                    "troughrelief": "flat",
                    "darkcolor": "#A0A0A0",
                    "relief": "ridge"
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
                    "background": "#e5e5e5",
                    "foreground": "black",
                    "fieldbackground": "#e5e5e5",
                    "insertborderwidth": 10,
                    "relief": "raised",
                    "bordercolor": "black",
                    "padding": (5,3,3,3),
                    "insertbackground": "blue",
                    "selectbackground": "#d2d2d2",
                    "selectforeground": "#4e4e4e",
                },
                "map": {
                    "insertbackgroud": [("focus", "white")]
                }
            },
            "Label.TEntry": {
                "layout": [
                    ("Entry.field", {"sticky": "nswe", "border": 0,  "children": [
                        ("Entry.padding", {"sticky": "nswe",  "children": [
                            ("Entry.label", {"sticky": "nswe"}),
                            ("Entry.textarea", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "background": "#e5e5e5",
                    "foreground": "#003726",
                    "fieldbackground": "#e5e5e5",
                    "insertborderwidth": 10,
                    "relief": "flat",
                    "bordercolor": "#e5e5e5",
                    "padding": (5,3,3,3),
                    "insertbackground": "#e5e5e5",
                },
                "map": {
                    "insertbackgroud": [("focus", "#e5e5e5")]
                }
            },
            "Titulo.TLabel": {
                "layout": [
                    ("Label.border", {"sticky": "nswe", "children":[
                        ("Label.padding", {"sticky": "nswe", "children": [
                            ("Label.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure":{
                    "font": ("Arial", 16, "bold")
                }
            },
            "TCombobox": {
                "layout": [
                    ("Combobox.border", {"sticky": "nswe", "children":[
                        ("Combobox.padding", {"sticky": "nswe", "children": [
                            ("Combobox.label", {"sticky": "nswe"}),
                            ("Combobox.textarea", {"sticky": "nswe"}),
                            ("Combobox.downarrow", {"side": "right"}),
                        ]})
                    ]})
                ],
                "configure": {
                    "fieldbackground": "#e5e5e5",
                    "background": "#e5e5e5",
                    "padding": (5,5,5,5),
                    "selectbackground": "",
                    "selectforeground": "#333333",
                    "foreground": "#333333"
                },
                "map": {
                    "bordercolor": [("focus", "green")],
                    "background": [("active", "black")],
                    "arrowcolor": [("active", "blue")],
                    "foreground": [("readonly", "#333333"), ("!readonly", "#333333"), ("active", "#333333")],
                    "fieldbackground": [("readonly", "#333333")]
                }
            },
            "TCombobox.Label": {
                "configure": {
                    "foreground": "black"
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
                    "background": "#dadada"
                }
            },
            "TextAdvertencia.TLabel":{
                "layout": [
                    ("Label.border", {"sticky": "nswe", "children":[
                        ("Label.padding", {"sticky": "nswe", "children": [
                            ("Label.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure":{
                    "font": ("Arial", 10),
                    "foreground": '#121212',
                    "background": "#dadada",
                    "padding": (5,5,15,5)
                    
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
                    "background": "#dadada",
                    "padding": (5,5,15,5)
                }
            },
            "Completado.TLabel":{
                "layout": [
                    ("Label.border", {"sticky": "nswe", "children":[
                        ("Label.padding", {"sticky": "nswe", "children": [
                            ("Label.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "font": ("Arial", 16, "bold"),
                    "foreground": "green",
                    "background": "#dadada",
                    "padding": (5,5,15,5)
                    
                }
            },
            "TextCompletado.TLabel":{
                "layout": [
                    ("Label.border", {"sticky": "nswe", "children":[
                        ("Label.padding", {"sticky": "nswe", "children": [
                            ("Label.label", {"sticky": "nswe"})
                        ]})
                    ]})
                ],
                "configure": {
                    "font": ("Arial", 10),
                    "foreground": '#121212',
                    "background": "#dadada"
                }
            }
        }
    )