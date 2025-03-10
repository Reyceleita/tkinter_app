def neon_theme(style):
    style.theme_create(
        "Neon_theme",
        parent="default",  
        settings={
            ".": {
                "configure": {
                    "background": "#101010", 
                    "foreground": "#0FF0FC"
                }
            },
            "Treeview":{
                "configure": {
                    "background": "#202020",
                    "fieldbackground": "#0FF0FC",
                }
            },
            "TButton": {
                "configure": {
                    "background": "#FF00FF",
                    "foreground": "black",
                    "bordercolor": "#FF4500"
                },
                "map": {
                    "background": [("active", "#FF4500")]
                }
            }
        }
    )