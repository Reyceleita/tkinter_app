import tkinter as tk 
from tkinter import *
from tkinter import ttk

from controller.data.mostrar import *
from controller.data.obtener_data import *
from controller.tecnicos.insertar import *
from view.tecnicos.edit_tecnico import *

#Pestaña para el manejo de técnicos
class TabTecnicos(ttk.Frame):
    def __init__(self , parent):
        super().__init__(parent)
        
        #Configuración de la pestaña
        self.columnconfigure(3, weight=1)
        self.rowconfigure(3)
        
        #Variables para almacenar información de técnicos
        self.cargo_id = {}
        self.nombre = StringVar()
        self.fecha_ingreso = StringVar()
        self.fecha_salida = StringVar()
        
        #Columnas para la tabla
        columnas = (
            'Nombre', 'Cargo', 'Fecha de ingreso', 'Fecha de salida', 
            'Tickets asignados', 'Tickets cerrados', 'Estado'
        )
        
        #etiquetas informativas
        ttk.Label(self, text='Registrar técnico').grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(self, text='Nombre:').grid(row=1, column=0, columnspan=1, padx=20, pady=5, sticky='w' )
        ttk.Label(self, text='Cargo:', font=('Arial', 10)).grid(row=2, column=0, columnspan=1, padx=20, pady=5, sticky='w')
        ttk.Label(self, text='Fecha de ingreso:', font=('Arial', 10)).grid(row=3, column=0, columnspan=1, padx=20, pady=5, sticky='w')
        ttk.Label(self, text='Fecha de salida:', font=('Arial', 10)).grid(row=4, column=0, columnspan=1, padx=20, pady=5, sticky='w')
        ttk.Label(self, text='Tecnicos', font=('Arial', 14)).grid(row=0, column=3, columnspan=1, pady=5, padx=250, sticky='e')
        
        #Campos de entrada
        self.cargo_campo = ttk.Combobox(self, state='readonly', font=('Arila', 9))
        self.nombre_campo = ttk.Entry(self, font=('Arial', 9), width=23, textvariable=self.nombre)
        self.ingreso_campo = ttk.Entry(self, width=23, font=('Arial', 9), textvariable=self.fecha_ingreso)
        self.salida_campo = ttk.Entry(self, width=23, font=('Arial', 9), textvariable=self.fecha_salida)
        
        #Configuración de tabla y scrollbar
        scrolly = ttk.Scrollbar(self, orient="vertical")
        self.tabla_tecnicos = ttk.Treeview(
            self, columns=columnas, show="headings",
            yscrollcommand=scrolly, selectmode='browse'
        )
        
        #Posicionamiento de widgets en la interfaz
        self.nombre_campo.grid(row=1, column=1, columnspan=2, pady=5, sticky='w')
        self.cargo_campo.grid(row=2, column=1, columnspan=2)
        self.ingreso_campo.grid(row=3, column=1, columnspan=2, pady=5, sticky='w')
        self.salida_campo.grid(row=4, column=1, columnspan=2, pady=5, sticky='w')
        self.tabla_tecnicos.grid(row=1, column=3, columnspan=1, rowspan=5, sticky='E', padx=17)
        scrolly.grid(row=1, column=3, rowspan=5, sticky="nse")
        scrolly.config(command=self.tabla_tecnicos.yview)
        
        #Configuración de encabezados de columna
        for columna in columnas:
            self.tabla_tecnicos.heading(columna, text=columna, command=lambda c=columna: ordenar_tabla(self.tabla_tecnicos, c, False, columnas))
            self.tabla_tecnicos.column(columna, width=100)
        
        #Vincular selección de la tabla a una función
        self.tabla_tecnicos.bind("<<TreeviewSelect>>", self.obtener_tecnico)
        
        #Botón de acción
        ttk.Button(self, text='Crear', command=lambda: crear_tecnico(self.cargo_id, self.cargo_campo.get(), 
                                                                    self.ingreso_campo.get(), self.nombre_campo.get(), self.salida_campo.get(), 
                                                                    self.tabla_tecnicos, self.nombre_campo, self.ingreso_campo, self.salida_campo, self.cargo_campo, self )).grid(row=5, column=2, columnspan=1, pady=5, sticky='E')
        
        #Cargar datos en la taba y en combobox
        cargar_tecnicos(self.tabla_tecnicos)
        cargar_cargo(self.cargo_id ,self.cargo_campo)
    
    #Crear ventana de edición según selección en la tabla
    def obtener_tecnico(self, event):
        tecnico = self.tabla_tecnicos.selection()[0]
        nombre = str(self.tabla_tecnicos.item(tecnico, 'values')[0])
        EditarTecnico(self, nombre, self.tabla_tecnicos, self.cargo_id)