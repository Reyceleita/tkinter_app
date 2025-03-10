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
            "TButton": {
                "configure": {
                    "background": "#007BFF",
                    "foreground": "white",
                    "bordercolor": "#0056b3"
                },
                "map": {
                    "background": [("active", "#0056b3")]
                }
            }
        }
    )