import tkinter as tk
from tkinter import *
from tkinter import ttk


from controller.tickets.consultar import *
from controller.tickets.subir_tickets import *
from view.tickets.editar_ticket import *

#Pestaña para tickets
class TabTickets(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Configuración de pestaña
        self.grid(row=0, column=0, sticky='nswe')
        self.columnconfigure(4, weight=1)
        self.rowconfigure(7, weight=1)
        self.conteo = IntVar(value=0) #Definición de variable 
        
        #Columnas para tabla
        columnas = (
            'Código', 'Título', 'Estado', 'Fecha de apertura', 'Fecha límite', 
            'Categoría', 'Localización', 'Técnico encargado','Solucion', 
            'Script', 'Fecha de solución', 'Observaciones', 'Revisado'
        )
        
        #Etiquetas informativas
        ttk.Label(self, text='Registro de tickets').grid(row=0, column=0, sticky='wn')
        ttk.Label(self, textvariable=self.conteo, font=('Arial', 10)).grid(row=2, column=2, sticky='e')
        ttk.Label(self, text='Se muestran: ', font=('Arial', 10)).grid(row=2, column=2, padx=30, sticky='e')
        ttk.Label(self, text='Filtro:', font=('Arial', 10)).grid(row=2, column=0, padx=10, sticky='w')
        
        #Variables y elementos de entrada
        id_filtro = ttk.Entry(self, width=33)
        columna_filtro = ttk.Combobox(self, state='readonly', values=columnas)
        
        #Configuración de tabla y scrollbar
        scrolly = ttk.Scrollbar(self, orient='vertical')
        self.tabla = ttk.Treeview(
            self, columns=columnas, show='headings', height=20,
            yscrollcommand=scrolly.set, selectmode='browse'
        )
        
        #Posisionamiento de widgets en la interfaz
        columna_filtro.grid(row=3, column=0, padx=10, sticky='w')
        id_filtro.grid(row=3, column=0, padx=10, sticky='w')
        self.tabla.grid(row=4, column=0, rowspan=3, columnspan=3, padx=10, pady=10, sticky='we')
        scrolly.grid(row=4, column=2, rowspan=3, sticky='ens')
        scrolly.config(command=self.tabla.yview) #Vincular scrollbar a la tabla
        
        #Botones de acción
        ttk.Button(self, text='Filtrar', command= lambda: filtar_id(id_filtro, columna_filtro, self.tabla, self.conteo) ).grid(row=3, column=0, pady=5, padx=3)
        ttk.Button(self, text='Subir archivo', command= lambda: subir_tickets(self.tabla)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        #Configuración de encabezados de la tabla
        for columna in columnas:
            self.tabla.heading(columna, text=columna, command= lambda c=columna, cols = columnas: ordenar_tabla(self.tabla, c, False, cols))
            self.tabla.column(column=columna, width=100)
            
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