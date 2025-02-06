import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.abiertos.subir import *
from controller.data.mostrar import *
from controller.abiertos.consultar import *
from view.abiertos.edit_abiertos import *

class TabAbiertos(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Se muestra la pestaña
        self.grid(row=0, column=0, sticky='nswe')
        
        #Variable de contador de registros mostrados
        self.conteo = tk.IntVar(value=0)
        
        
        #Columnas qe tiene la tabla
        columnas = (
            'Código', 'Título', 'Fecha de apertura', 'Fecha límite', 
            'Categoría', 'Técnico encargado','Solucion', 
            'Script', 'Fecha de solución', 'Observaciones', 'Estado','Revisado'
        )
        
        #------------------------------------------Widgets------------------------------------------#
        ttk.Label(self, text='Tickets abiertos', font=('Arial', 14)).grid(row=0, column=1, sticky='wn')
        ttk.Button(self, text='Cerrar', command='').grid(row=3, column=1, padx=5, pady=5)
        
            #filtro
        ttk.Label(self, text='Fitro: ', font=('Arial', 10)).grid(row=2, column=0, padx=10, sticky='w')
        
        self.valor = ttk.Entry(self, width=33)
        self.valor.grid(row=4, column=0, padx=10, sticky='w')
        self.columna = ttk.Combobox(self, state='readonly', values=columnas)
        self.columna.grid(row=3, column=0, padx=10, sticky='w')
        self.button = ttk.Button(self, text='Filtrar', command= lambda: filtar_id_abiertos(self.valor.get(), self.columna.get(), self.tabla, self.conteo))
        self.button.grid(row=4, column=1, pady=5, padx=3)

            #Mostrar conteo de registros mostrados
        ttk.Label(self, text='Se muestran: ', font=('Arial', 10)).grid(row=2, column=3, padx=20, sticky='e')
        ttk.Label(self, textvariable=self.conteo, font=('Arial', 10)).grid(row=2, column=3, sticky='e', padx=5)
        
        #Tabla para mostrar registros
        scrolly = ttk.Scrollbar(self, orient='vertical')
        self.tabla = ttk.Treeview(
            self, columns=columnas, show='headings', height=20,
            yscrollcommand=scrolly.set, selectmode='browse'
        )
        
        self.tabla.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='we')
        scrolly.grid(row=5, column=3, rowspan=1, sticky='ens')
        
        scrolly.config(command=self.tabla.yview)
        
        #Cargar columnas a la tabla
        for columna in columnas:
            self.tabla.heading(columna, text=columna, command=lambda c=columna, cols=columnas: ordenar_tabla(self.tabla, c, False, cols))
            self.tabla.column(column=columna, width=100)
            
        ttk.Button(self, text='Subir archivo', command=lambda: subir_abiertos(self.tabla)).grid(row=1, column=0, padx=5, sticky='w')
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_ticket)
        mostrar_datos(query_datos_activos(), self.tabla)
        self.conteo.set(mostrar_datos(query_datos_activos(), self.tabla))
        
    def obtener_ticket(self, event):
        ticket = self.tabla.selection()[0]
        id_ticket = self.tabla.item(ticket, 'values')[0]
        titulo_ticket = self.tabla.item(ticket, 'values')[1]
        EditarAbiertos(self, id_ticket, titulo_ticket, self.tabla)
    