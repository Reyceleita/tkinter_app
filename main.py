from tkinter import *
from tkinter import ttk
import tkinter as tk

from model.execution import *
from view.abiertos.abiertos import *
from view.tickets.tickets import *
from view.tecnicos.tecnicos import *
from view.styles.dark_mode import *
from view.styles.solarized import *
from view.styles.neon import *
from view.styles.light_mode import *
from settings.settings import *
from view.settings.settings import *

# Se crea app principal
class App(tk.Tk):
    instancia = None

    def __init__(self):
        super().__init__()

        self.style = ttk.Style()
        dark_theme(self.style)
        light_theme(self.style)
        solarized_theme(self.style)
        neon_theme(self.style)

        # Configura ventana principal
        self.title("Gestión de tickets")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}-0+0")

        # Cear manejo de pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nswe")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Iniciar y agregan pestañas
        self.abiertos = TabAbiertos(self.notebook)
        self.tickets = TabTickets(self.notebook)
        self.notebook.add(self.abiertos, text="Abiertos")
        self.notebook.add(self.tickets, text="Tickets")
        ttk.Button(self.notebook, text="Ajustes", command=lambda: Ajustes(self)).place(
            relx=0.97, rely=0.87, anchor="ne"
        )
        # Vincular evento de pestañas
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_selected)
        self.aplicar_tema()

    # Cargar datos al cambiar de pestaña
    def on_tab_selected(self, event):
        pestaña = self.notebook.index(self.notebook.select())

        if pestaña == 0:
            mostrar_datos(query_datos_activos(), self.abiertos.traer_tabla())
        elif pestaña == 1:
            mostrar_datos(query_datos(), self.tickets.traer_tabla())

    #Aplicar tema guardado
    def aplicar_tema(self):
        tema = cargar_config()
        bg = tema["background"]
        fg = tema["foreground"]
        list_bg = tema["listbg"]
        list_fg = tema["listfg"]
        tema = tema["tema"]
        self.style.theme_use(tema)

        self.option_add("*background", bg)
        self.option_add("*foreground", fg)
        self.option_add("*TCombobox*Listbox.background", list_bg)
        self.option_add("*TCombobox*Listbox.foreground", list_fg)


# Ejecución de aplicación
if __name__ == "__main__":
    first_execute()
    app = App()
    app.mainloop()
