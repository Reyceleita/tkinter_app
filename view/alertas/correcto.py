import tkinter as tk
from tkinter import *
from tkinter import ttk

#Ventana de alerta personalizada
class Completado(tk.Toplevel):
    def __init__(self, parent, texto):
        super().__init__(parent)
        
        #Definir variable de texto a usar
        self.texto = StringVar()
        self.texto.set(texto)
        
        #Configuraciones de ventana
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)
        self.grid()
        self.configure(bg='#dadada', bd=10, relief='raised')

        #Widgets que se mustran
        ttk.Label(self, text='Completado', style='Completado.TLabel').grid(column=0, row=0, columnspan=2)
        ttk.Label(self, textvariable=self.texto, style="TextCompletado.TLabel").grid(column=0, row=1, padx=15)
        ttk.Button(self, text='Aceptar', command=self.destroy).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        
        #Definir dimensiones de la alerta
        self.update_idletasks()
        self.geometry("")
        ancho = self.winfo_reqwidth()
        alto = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.grab_set()