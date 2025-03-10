import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.data.obtener_data import *
from controller.BD.insert import *

class InsertData():
    def __init__(self, frame):
        self.campo_list = {}
        self.fra = frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        self.tablas = {
            "Cargos": "cargos",
            "Scripts": "scripts",
            "Forma de solución": "forma_solucion"
        }
        
        ttk.Label(frame, text='Agregar datos').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text='Tabla:').grid(row=1, column=0, padx=10, pady=10)
        
        self.tabla = ttk.Combobox(frame, values=('Cargos', 'Scripts', 'Forma de solución'), state='readonly')
        self.nuevo = tk.Entry(frame)
        
        ttk.Button(frame, text='Agregar', command= self.agregar).grid(row=4, column=3, padx=10, pady=10)
        
        self.nuevo.grid(row=4, column=0, padx=10, pady=10)
        self.tabla.grid(row=2, column=0, padx=10, pady=10)
        self.tabla.bind('<<ComboboxSelected>>', )

    def agregar(self):
        tabla = self.tabla.get()
        tabla = self.tablas.get(tabla)
        nombre = self.nuevo.get()
        if tabla == 'cargos':
            campo = 'cargo'
        elif tabla == 'scripts':
            campo = 'script'
        elif tabla == 'forma_solucion':
            campo = 'solucion'
        insert(self.fra, nombre, tabla, campo)