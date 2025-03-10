import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.data.obtener_data import *
from controller.BD.delete import *

class DeleteData():
    def __init__(self, frame):
        self.campo_list = {}
        self.fra = frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        ttk.Label(frame, text='Eliminar dato').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text='Tabla:').grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(frame, text='Registro a eliminar.').grid(row=1, column=1, padx=10, pady=10)
        
        self.tabla = ttk.Combobox(frame, values=('Cargos', 'Scripts', 'Forma de solución'), state='readonly')
        self.campo = ttk.Combobox(frame, values='', state='readonly')
        
        ttk.Button(frame, text='Eliminar', command= self.elimina).grid(row=4, column=3, padx=10, pady=10)
        
        self.tabla.grid(row=2, column=0, padx=10, pady=10)
        self.campo.grid(row=2, column=1, padx=10, pady=10)
        self.tabla.bind('<<ComboboxSelected>>', self.cargar_datos)

    def cargar_datos(self, event):
        self.tablas = {
            "Cargos": "cargos",
            "Scripts": "scripts",
            "Forma de solución": "forma_solucion"
        }
        
        tabla = self.tabla.get()
        
        tabla = self.tablas.get(tabla)
        
        cargar_tablas(self.campo, self.campo_list, tabla)
    
    def elimina(self):
        tabla = self.tabla.get()
        tabla = self.tablas.get(tabla)
        combobox = self.campo.get()
        id = obtener_campo_lista(self.campo_list, combobox)
        if tabla == 'cargos':
            valor = 'id_cargo'
        elif tabla == 'scripts':
            valor = 'id_script'
        elif tabla == 'forma_solucion':
            valor = 'id_solucion'
        delete(self.fra, id, tabla, valor)