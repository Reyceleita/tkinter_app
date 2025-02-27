import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.abiertos.subir import *
from controller.data.mostrar import *
from controller.abiertos.consultar import *
from view.abiertos.edit_abiertos import *
from controller.abiertos.filtro import *
from controller.abiertos.cerrar_tickets import *

#Pestaña de tickets abiertos
class TabAbiertos(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Columnas de la tabla
        self.columnas = (
            'Código', 'Título', 'Fecha de apertura', 'Fecha límite', 
            'Categoría', 'Técnico encargado','Solucion', 
            'Script', 'Fecha de solución', 'Observaciones', 'Estado','Revisado'
        )
        
        #Configuración de pestaña
        self.grid(row=0, column=0, sticky='nswe')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)
        for i in range(len(self.columnas) + 1): 
            self.grid_columnconfigure(i, weight=1)
            
        #Variable para alamcenar datos a usar
        self.conteo = tk.IntVar(value=0)
        self.filters = {}
        self.contador = StringVar()
        self.contador.set(f'Se muestran: {self.conteo.get()}')
        
        
        #Etiquetas informativas
        ttk.Label(self, text='Tickets abiertos', font=('Arial', 14)).grid(row=0, column=5, sticky='wn')
        ttk.Label(self, text='Se muestran: ', font=('Arial', 10)).grid(row=2, column=11, padx=20, sticky='e')
        ttk.Label(self, textvariable=self.conteo, font=('Arial', 10)).grid(row=2, column=11, sticky='e', padx=5)
        
        
        #Configuración de tabla y scroll
        scrolly = ttk.Scrollbar(self, orient='vertical')
        self.tabla = ttk.Treeview(
            self, columns=self.columnas, show='headings', height=20,
            yscrollcommand=scrolly.set, selectmode='browse'
        )
        
        #Posicionamiento de widgets
        self.tabla.grid(row=5, column=0, columnspan=len(self.columnas), padx=10, pady=10, sticky='we')
        scrolly.grid(row=5, column=len(self.columnas), rowspan=1, sticky='ens')
        scrolly.config(command=self.tabla.yview) #Vincular scrollbar a la tabla
        
        #Configuración de encabezados de la tabla
        for columna in self.columnas:
            self.tabla.heading(columna, text=columna.capitalize(), command=lambda c=columna, cols=self.columnas: ordenar_tabla(self.tabla, c, False, cols))
            self.tabla.column(column=columna, width=100)
        
        for i, columna in enumerate(self.columnas):
            entry = ttk.Entry(self, width=10)
            entry.grid(row=4, column=i, pady=5, padx=5, sticky='ew')
            entry.bind("<KeyRelease>", self.filtrar)  
            self.filters[columna] = entry 
        
        #Vincular selección de la tabla a una función
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_ticket)
        
        #Botones de acción
        ttk.Button(self, text='Subir archivo', command=self.subir_archivo).grid(row=1, column=0, padx=5, sticky='w')
        ttk.Button(self, text='Cerrar revisados', command=lambda: cerrar_abierto(self.tabla, self)).grid(row=3, column=0, padx=5, pady=5, sticky='w')
        
        #Cargar datos en la tabla y actualizar conteo 
        mostrar_datos(query_datos_activos(), self.tabla)
        self.conteo.set(mostrar_datos(query_datos_activos(), self.tabla))
        self.contador.set(f'Se muestran: {self.conteo.get()}')
        
    #Llamar ventana para edición de datos
    def obtener_ticket(self, event):
        ticket = self.tabla.selection()[0]
        id_ticket = self.tabla.item(ticket, 'values')[0]
        titulo_ticket = self.tabla.item(ticket, 'values')[1]
        EditarAbiertos(self, id_ticket, titulo_ticket, self.tabla)
        self.contador.set(f'Se muestran: {self.conteo.get()}')
    
    #Filtrar segúnlo escito en los campos Entry
    def filtrar(self, event):
        filter_values = {col: self.filters[col].get() for col in self.columnas}
        filtro(tabla=self.tabla, filter=filter_values)
        self.conteo.set(mostrar_datos(filtro(self.tabla, filter_values), self.tabla))
        self.contador.set(f'Se muestran: {self.conteo.get()}')
    
    def subir_archivo(self):
        subir_abiertos(self.tabla, self)
        self.conteo.set(mostrar_datos(query_datos_activos(), self.tabla))
        self.contador.set(f'Se muestran: {self.conteo.get()}')