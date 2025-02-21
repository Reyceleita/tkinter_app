import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.abiertos.subir import *
from controller.data.mostrar import *
from controller.abiertos.consultar import *
from view.abiertos.edit_abiertos import *
from controller.abiertos.filtro import *

#Pestaña de tickets abiertos
class TabAbiertos(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Configuración de pestaña
        self.grid(row=0, column=0, sticky='nswe')
        self.columnconfigure(3, weight=1)
        self.rowconfigure(6, weight=1)
        
        #Variable para guardar conteo de registros
        self.conteo = tk.IntVar(value=0)
        self.filters = {}
        
        #Columnas de la tabla
        self.columnas = (
            'Código', 'Título', 'Fecha de apertura', 'Fecha límite', 
            'Categoría', 'Técnico encargado','Solucion', 
            'Script', 'Fecha de solución', 'Observaciones', 'Estado','Revisado'
        )
        
        #Etiquetas informativas
        ttk.Label(self, text='Tickets abiertos', font=('Arial', 14)).grid(row=0, column=1, sticky='wn')
        ttk.Label(self, text='Fitro: ', font=('Arial', 10)).grid(row=2, column=0, padx=10, sticky='w')
        ttk.Button(self, text='Cerrar', command='').grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(self, text='Se muestran: ', font=('Arial', 10)).grid(row=2, column=3, padx=20, sticky='e')
        ttk.Label(self, textvariable=self.conteo, font=('Arial', 10)).grid(row=2, column=3, sticky='e', padx=5)
        
        #Campos de entrada
        self.valor = ttk.Entry(self, width=33)
        self.columna = ttk.Combobox(self, state='readonly', values=self.columnas)
        self.button = ttk.Button(self, text='Filtrar', command= lambda: filtar_id_abiertos(self.valor.get(), self.columna.get(), self.tabla, self.conteo))
        
        
        #Configuración de tabla y scroll
        scrolly = ttk.Scrollbar(self, orient='vertical')
        self.tabla = ttk.Treeview(
            self, columns=self.columnas, show='headings', height=20,
            yscrollcommand=scrolly.set, selectmode='browse'
        )
        
        #Posicionamiento de widgets
        self.valor.grid(row=4, column=0, padx=10, sticky='w')
        self.columna.grid(row=3, column=0, padx=10, sticky='w')
        self.button.grid(row=4, column=1, pady=5, padx=3)
        self.tabla.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='we')
        scrolly.grid(row=5, column=3, rowspan=1, sticky='ens')
        scrolly.config(command=self.tabla.yview) #Vincular scrollbar a la tabla
        
        #Configuración de encabezados de la tabla
        for columna in self.columnas:
            self.tabla.heading(columna, text=columna.capitalize(), command=lambda c=columna, cols=self.columnas: ordenar_tabla(self.tabla, c, False, cols))
            self.tabla.column(column=columna, width=100)
            
            self.palabra = ttk.Entry(self)
            self.palabra.grid()
            self.palabra.bind("<KeyRelease>", self.filtrar)
            self.filters[columna] = self.palabra
        
        #Vincular selección de la tabla a una función
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_ticket)
        
        #Botón de acción
        ttk.Button(self, text='Subir archivo', command=lambda: subir_abiertos(self.tabla)).grid(row=1, column=0, padx=5, sticky='w')
        
        #Cargar datos en la tabla y actualizar conteo 
        mostrar_datos(query_datos_activos(), self.tabla)
        self.conteo.set(mostrar_datos(query_datos_activos(), self.tabla))
        
    #Llamar ventana para edición de datos
    def obtener_ticket(self, event):
        ticket = self.tabla.selection()[0]
        id_ticket = self.tabla.item(ticket, 'values')[0]
        titulo_ticket = self.tabla.item(ticket, 'values')[1]
        EditarAbiertos(self, id_ticket, titulo_ticket, self.tabla)
    
    def filtrar(self, event):
        filter_values = {col: self.filters[col].get() for col in self.columna}
        nose(filter=filter_values)