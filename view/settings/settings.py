import tkinter as tk
from tkinter import *
from tkinter import ttk

from view.settings.preferences import *
from view.settings.data import *

#Ventana de configuraciones de app
class Ajustes(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Crear y agregar franes
        self.grid()
        self.columnconfigure(5, weight=1)
        self.rowconfigure(5, weight=1)
        opciones = ttk.Frame(self)
        opciones.grid(row=1, column=0)
        opciones.rowconfigure(5, weight=1)
        contenido = ttk.Frame(self)
        contenido.grid(row=1, column=1)
        contenido.rowconfigure(5, weight=1)
        
        #Elementos visuales de la app
        ttk.Label(self, text='Configuraciones').grid(row=0, column=0, sticky='we', columnspan=3)
        
        ttk.Button(opciones, text='Datos', command=lambda: Datos(contenido)).grid(row=0, column=0, padx=10, pady=15, sticky='w')
        ttk.Button(opciones, text='Preferencias', command=lambda: Preferencias(contenido)).grid(row=1, column=0, padx=10, sticky='w')
        ttk.Separator(self, orient='vertical').grid(row=1, column=0, rowspan=10, sticky='ens')
        
        #Redimensión y cambio de posición de la ventana
        self.geometry("")
        x = (self.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.winfo_screenheight() // 2) - (500 // 2)
        self.geometry(f"{800}x{500}+{x}+{y}")
        self.grab_set()