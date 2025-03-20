import tkinter as tk
from tkinter import *
from tkinter import ttk


class AdverteciaAlerta(tk.Toplevel):
    def __init__(self, parent, texto):
        super().__init__(parent)

        # Definir variable de texto a usar
        self.texto = StringVar()
        self.texto.set(texto)

        # Configuraciones de ventana
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)
        self.grid()
        self.configure(bg="#dadada", bd=10, relief="raised")

        # Widgets que se mustran
        ttk.Label(self, text="Advertencia", style="Advertencia.TLabel").grid(
            column=0, row=0, columnspan=2
        )
        ttk.Label(self, textvariable=self.texto, style="TextAdvertencia.TLabel").grid(
            column=0, row=1
        )
        ttk.Button(self, text="Cerrar", command=self.destroy).grid(
            column=0, row=2, pady=5, sticky="e"
        )

        # Definir dimensiones de la alerta
        self.update_idletasks()
        self.geometry("")
        ancho = self.winfo_reqwidth()
        alto = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.grab_set()
