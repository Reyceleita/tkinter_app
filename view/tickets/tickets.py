import tkinter as tk
from tkinter import *
from tkinter import ttk


from controller.tickets.consultar import *
from controller.tickets.subir_tickets import *
from view.tickets.editar_ticket import *
from controller.tickets.filtro import *

#Pestaña para tickets
class TabTickets(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Columnas para tabla
        self.columnas = (
            'Código', 'Título', 'Estado', 'Fecha de apertura', 'Fecha límite', 
            'Categoría', 'Localización', 'Técnico encargado','Solucion', 
            'Script', 'Fecha de solución', 'Observaciones', 'Revisado'
        )
        
        #Configuración de pestaña
        self.grid(row=0, column=0, sticky='nswe')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(7, weight=1)
        self.conteo = IntVar(value=0) #Definición de variable
        for i in range(len(self.columnas)+ 1):
            self.grid_columnconfigure(i, weight=1)
        
        #Variable para alamcenar datos a usar
        self.conteo = tk.IntVar(value=0)
        self.filters = {}
        
        #Etiquetas informativas
        ttk.Label(self, text='Registro de tickets').grid(row=0, column=0, sticky='wn')
        ttk.Label(self, textvariable=self.conteo, font=('Arial', 10)).grid(row=2, column=2, sticky='e')
        ttk.Label(self, text='Se muestran: ', font=('Arial', 10)).grid(row=2, column=2, padx=30, sticky='e')
        
        #Configuración de tabla y scrollbar
        scrolly = ttk.Scrollbar(self, orient='vertical')
        self.tabla = ttk.Treeview(
            self, columns=self.columnas, show='headings', height=20,
            yscrollcommand=scrolly.set, selectmode='browse'
        )
        
        #Posisionamiento de widgets en la interfaz
        self.tabla.grid(row=5, column=0, rowspan=2, columnspan=len(self.columnas), padx=10, pady=10, sticky='we')
        scrolly.grid(row=5, column=13, rowspan=2, sticky='ens')
        scrolly.config(command=self.tabla.yview) #Vincular scrollbar a la tabla
        
        #Boton de acción
        ttk.Button(self, text='Subir archivo', command= lambda: subir_tickets(self.tabla)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        #Configuración de encabezados de la tabla
        for columna in self.columnas:
            self.tabla.heading(columna, text=columna, command= lambda c=columna, cols = self.columnas: ordenar_tabla(self.tabla, c, False, cols))
            self.tabla.column(column=columna, width=100)
        
        for i, columna in enumerate(self.columnas):
            entry = ttk.Entry(self, width=10)
            entry.grid(row=4, column=i, padx=5, pady=5, sticky='ew')
            entry.bind('<KeyRelease>', self.filtrar)
            self.filters[columna] = entry
            
        #Vincular selección de la tabla a una función
        self.tabla.bind('<<TreeviewSelect>>', self.obtener_ticket)
        
        #Cargar datos en la tabla y actualizar conteo 
        mostrar_datos(query_datos(), self.tabla)
        self.conteo.set(mostrar_datos(query_datos(), self.tabla))
        
    #Llamar ventana para edición de datos
    def obtener_ticket(self, event):
        ticket = self.tabla.selection()[0]
        id_ticket = self.tabla.item(ticket, "values")[0]
        titulo_ticket = self.tabla.item(ticket, "values")[1]
        EditarTicket(self, id_ticket, titulo_ticket, self.tabla)
    
    def filtrar(self, event):
        filter_values = {col: self.filters[col].get() for col in self.columnas}
        filtro(self.tabla, filter_values)
        self.conteo.set(mostrar_datos(filtro(self.tabla, filter_values), self.tabla))