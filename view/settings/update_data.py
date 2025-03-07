import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.data.obtener_data import *
from controller.BD.update import *

#Actualizar tablas 
class UpdateTablas():
    def __init__(self, frame):
        self.campo_list = {}
        self.fra = frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        ttk.Label(frame, text='Modificar tablass').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text='Tabla:').grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(frame, text='Registro a modificar:').grid(row=1, column=1, padx=10, pady=10)
        ttk.Label(frame, text='Nuevo valor:').grid(row=3, column=0, padx=10, pady=10)
        
        self.tabla = ttk.Combobox(frame, values=('Cargos', 'Scripts', 'Forma de solución'), state='readonly')
        self.campo = ttk.Combobox(frame, values='', state='readonly')
        self.nuevo = ttk.Entry(frame)
        
        ttk.Button(frame, text='Actualizar', command= self.actualiza).grid(row=4, column=3, padx=10, pady=10)
        
        self.nuevo.grid(row=4, column=0, padx=10, pady=10)
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
    
    def actualiza(self):
        
        tabla = self.tabla.get()
        tabla = self.tablas.get(tabla)
        nombre = self.nuevo.get()
        combobox = self.campo.get()
        id = obtener_campo_lista(self.campo_list, combobox)
        if tabla == 'cargos':
            campo = 'cargo'
            valor = 'id_cargo'
        elif tabla == 'scripts':
            campo = 'script'
            valor = 'id_script'
        elif tabla == 'forma_solucion':
            campo = 'solucion'
            valor = 'id_solucion'
        update_valor(self.fra, id, nombre, tabla, campo, valor)