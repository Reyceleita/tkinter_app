import tkinter as tk
from tkinter import *
from tkinter import ttk

from view.settings.preferences import *
from view.settings.data import *
from view.tecnicos.tecnicos import *


# Ventana de configuraciones de app
class Ajustes(tk.Toplevel):
    def __init__(
        self,
        parent,
    ):
        super().__init__(parent)
        self.parent = parent

        # Configuracion inicial de ventana
        self.wm_attributes("-topmost", True)
        self.title("Cosas")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Crear manejo de pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nswe")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Crear y agregar pestañas
        self.datos = Datos(self.notebook)
        self.preferencias = Preferencias(self.notebook, self, parent)
        self.tecnicos = TabTecnicos(self.notebook)
        self.notebook.add(self.datos, text="Datos")
        self.notebook.add(self.preferencias, text="Preferencas")
        self.notebook.add(self.tecnicos, text="Técnicos")

        # Redimensión y cambio de posición de la ventana
        self.update_idletasks()
        self.geometry("")
        x = (self.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.winfo_screenheight() // 2) - (500 // 2)
        self.geometry(f"{800}x{500}+{x}+{y}")
        self.grab_set()
