import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.data.borrar_datos import *
from controller.data.exportToSCV import *

#Vista para elminar base de datos local
class Datos():
    def __init__(self, frame):
        
        for widget in frame.winfo_children():
            widget.destroy()
        
        ttk.Label(frame, text='Datos').grid(row=0, column=0, columnspan=2, sticky='we')
        ttk.Label(frame, text='Elimminar datos').grid(row=1, column=0, padx=5, sticky='w')
        ttk.Button(frame, text='Eliminar BD local', command=lambda: eliminar_db(frame)).grid(row=2, column=0, pady=10, padx=20)
        ttk.Button(frame, text='Exportar a csv', command=lambda: exportar_datos(frame)).grid(row=3, column=0, pady=10, padx=20)