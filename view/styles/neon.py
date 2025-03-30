# Definir tema Neon
def neon_theme(style):
    style.theme_create(
        "Neon_theme",
        parent="default",
        settings={
            ".": {"configure": {"background": "#101010", "foreground": "#0FF0FC"}},
            "Treeview": {
                "configure": {
                    "background": "#202020",
                    "fieldbackground": "#0FF0FC",
                }
            },
            "TButton": {
                "configure": {
                    "background": "#FF00FF",
                    "foreground": "black",
                    "relief": "raised",
                    "padding": (5, 0, 5, 0),
                    "borderwidth": 5,
                    "bordercolor": "#FF4500",
                },
                "map": {"background": [("active", "#c60fc6")]},
            },
            "Adv.TButton": {
                "layout": [
                    (
                        "Button.border",
                        {
                            "sticky": "nswe",
                            "border": 1,
                            "children": [
                                (
                                    "Button.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Button.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "background": "#fee642",
                    "foreground": "black",
                    "relief": "raised",
                    "bordercolor": "#005F46",
                    "padding": (5, 0, 5, 0),
                    "borderwidth": 5,
                },
                "map": {"background": [("active", "#cdb934")]},
            },
            "Scf.TButton": {
                "layout": [
                    (
                        "Button.border",
                        {
                            "sticky": "nswe",
                            "border": 10,
                            "children": [
                                (
                                    "Button.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Button.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "background": "#33d757",
                    "foreground": "black",
                    "relief": "raised",
                    "bordercolor": "#005F46",
                    "padding": (5, 0, 5, 0),
                    "borderwidth": 5,
                },
                "map": {"background": [("active", "#28a744")]},
            },
            "TScrollbar": {
                "layout": [
                    (
                        "Scrollbar.trough",
                        {
                            "children": [
                                ("Scrollbar.uparrow", {"side": "top", "sticky": "n"}),
                                (
                                    "Scrollbar.downarrow",
                                    {"side": "bottom", "sticky": "s"},
                                ),
                                ("Scrollbar.thumb", {"unit": "1", "sticky": "nswe"}),
                            ]
                        },
                    )
                ],
                "configure": {
                    "background": "#101010",
                    "troughcolor": "#101010",
                    "bordercolor": "#0FF0FC",
                    "arrowcolor": "#A0A0A0",
                    "troughrelief": "flat",
                    "darkcolor": "#A0A0A0",
                    "relief": "ridge",
                },
            },
            "TEntry": {
                "layout": [
                    (
                        "Entry.field",
                        {
                            "sticky": "nswe",
                            "border": 1,
                            "children": [
                                (
                                    "Entry.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Entry.label", {"sticky": "nswe"}),
                                            ("Entry.textarea", {"sticky": "nswe"}),
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "background": "#c7c7c7",
                    "foreground": "black",
                    "fieldbackground": "#c7c7c7",
                    "insertborderwidth": 10,
                    "relief": "raised",
                    "bordercolor": "black",
                    "padding": (5, 3, 3, 3),
                    "insertbackground": "blue",
                    # Agregaaaaaar lossss selecteddddd
                },
                "map": {"insertbackground": [("focus", "white")]},
            },
            "Label.TEntry": {
                "layout": [
                    (
                        "Entry.field",
                        {
                            "sticky": "nswe",
                            "border": 0,
                            "children": [
                                (
                                    "Entry.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Entry.label", {"sticky": "nswe"}),
                                            ("Entry.textarea", {"sticky": "nswe"}),
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "background": "#1E1E1E",
                    "foreground": "#00C896",
                    "fieldbackground": "#1E1E1E",
                    "insertborderwidth": 10,
                    "relief": "flat",
                    "bordercolor": "#1E1E1E",
                    "padding": (5, 3, 3, 3),
                    "insertbackground": "#1E1E1E",
                },
                "map": {"insertbackground": [("focus", "#1E1E1E")]},
            },
            "Titulo.TLabel": {
                "layout": [
                    (
                        "Label.border",
                        {
                            "sticky": "nswe",
                            "children": [
                                (
                                    "Label.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Label.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {"font": ("Arial", 16, "bold")},
            },
            "TCombobox": {
                "layout": [
                    (
                        "Combobox.border",
                        {
                            "sticky": "nswe",
                            "children": [
                                (
                                    "Combobox.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Combobox.label", {"sticky": "nswe"}),
                                            ("Combobox.textarea", {"sticky": "nswe"}),
                                            ("Combobox.downarrow", {"side": "right"}),
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "fieldbackground": "#1E1E1E",
                    "background": "#1E1E1E",
                    "bordercolor": "white",
                    "padding": (5, 5, 5, 5),
                    "selectbackground": "",
                    "selectforeground": "#0FF0FC",
                },
                "map": {
                    "bordercolor": [("focus", "green")],
                    "background": [("active", "white")],
                    "arrowcolor": [("active", "blue")],
                    "fieldbackground": [("readonly", "#1E1E1E")],
                },
            },
            "Advertencia.TLabel": {
                "layout": [
                    (
                        "Label.border",
                        {
                            "sticky": "nswe",
                            "children": [
                                (
                                    "Label.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Label.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "font": ("Arial", 16, "bold"),
                    "foreground": "yellow",
                    "background": "#dadada",
                },
            },
            "TextAdvertencia.TLabel": {
                "layout": [
                    (
                        "Label.border",
                        {
                            "sticky": "nswe",
                            "children": [
                                (
                                    "Label.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Label.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "font": ("Arial", 10),
                    "foreground": "#121212",
                    "background": "#dadada",
                    "padding": (5, 5, 15, 5),
                },
            },
            "Error.TLabel": {
                "layout": [
                    (
                        "Label.border",
                        {
                            "sticky": "nswe",
                            "children": [
                                (
                                    "Label.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Label.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "font": ("Arial", 16, "bold"),
                    "foreground": "Red",
                    "background": "#dadada",
                    "padding": (5, 5, 15, 5),
                },
            },
            "Completado.TLabel": {
                "layout": [
                    (
                        "Label.border",
                        {
                            "sticky": "nswe",
                            "children": [
                                (
                                    "Label.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Label.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "font": ("Arial", 16, "bold"),
                    "foreground": "green",
                    "background": "#dadada",
                    "padding": (5, 5, 15, 5),
                },
            },
            "TextCompletado.TLabel": {
                "layout": [
                    (
                        "Label.border",
                        {
                            "sticky": "nswe",
                            "children": [
                                (
                                    "Label.padding",
                                    {
                                        "sticky": "nswe",
                                        "children": [
                                            ("Label.label", {"sticky": "nswe"})
                                        ],
                                    },
                                )
                            ],
                        },
                    )
                ],
                "configure": {
                    "font": ("Arial", 10),
                    "foreground": "#121212",
                    "background": "#dadada",
                },
            },
        },
    )
