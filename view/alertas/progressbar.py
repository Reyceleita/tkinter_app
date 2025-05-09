import tkinter as tk
from tkinter import *
from tkinter import ttk

#Alerta de cargando para procesos demorados
class Progressbar(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Crear y mostrar alerta
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)
        self.grid()
        self.configure(bg="#dadada", bd=10, relief="raised")

        # Widget de información
        ttk.Label(self, text="Leyendo archivo...", style="TextCompletado.TLabel").grid(
            row=0, column=0, pady=15, padx=15
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
