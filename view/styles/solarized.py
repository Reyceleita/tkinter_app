# Definir tema solarized
def solarized_theme(style):
    style.theme_create(
        "Solarized_theme",
        parent="default",
        settings={
            ".": {"configure": {"background": "#FDF6E3", "foreground": "#657B83"}},
            "Treeview": {
                "configure": {"background": "#e6e6e6", "bordercolor": "#fdedbd"}
            },
            "Treeview.Heading": {
                "configure": {
                    "background": "#FFFFFF",
                }
            },
            "TButton": {
                "configure": {
                    "background": "#268BD2",
                    "foreground": "white",
                    "bordercolor": "#073642",
                    "relief": "raised",
                    "padding": (5, 0, 5, 0),
                    "borderwidth": 5,
                },
                "map": {"background": [("active", "#2AA198")]},
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
                "map": {"background": [("active", "#ead43d")]},
            },
            "Scf.TButton": {
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
                    "background": "#33d757",
                    "foreground": "black",
                    "relief": "raised",
                    "bordercolor": "#005F46",
                    "padding": (5, 0, 5, 0),
                    "borderwidth": 5,
                },
                "map": {"background": [("active", "#2ec14e")]},
            },
            "TScrollbar": {
                "Layout": [
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
                    "background": "#FDF6E3",
                    "troughcolor": "#fcf0d1",
                    "bordercolor": "#E0E0E0",
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
                    "background": "#fcf0d1",
                    "foreground": "black",
                    "fieldbackground": "#ffdab0",
                    "insertborderwidth": 10,
                    "relief": "flat",
                    "bordercolor": "black",
                    "padding": (5, 3, 3, 3),
                    "insertbackground": "blue",
                    "selectbackground": "#c8c6c6",
                },
                "map": {"insertbackgroud": [("focus", "white")]},
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
                    "background": "#e6e6e6",
                    "foreground": "#657B83",
                    "fieldbackground": "#e6e6e6",
                    "insertborderwidth": 10,
                    "relief": "flat",
                    "bordercolor": "#e6e6e6",
                    "padding": (5, 3, 3, 3),
                    "insertbackground": "#e6e6e6",
                },
                "map": {"insertbackgroud": [("focus", "#e6e6e6")]},
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
                    "fieldbackground": "#e6e6e6",
                    "background": "#e6e6e6",
                    "foreground": "#657B83",
                    "borderclor": "#83860b",
                    "padding": (5, 5, 5, 5),
                    "selectbackground": "",
                    "selectforeground": "#657B83",
                },
                "map": {
                    "bordercolor": [("focus", "green")],
                    "background": [("active", "white")],
                    "arrowcolor": [("active", "blue")],
                    "fieldbackground": [("readonly", "#c3c3c3")],
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
