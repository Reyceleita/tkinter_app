import tkinter as tk
from tkinter import *
from tkinter import ttk


from controller.tickets.consultar import *
from controller.tickets.subir_tickets import *
from view.alertas.progressbar import Progressbar
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
        self.contador = StringVar()
        self.last_hover = None
        
        for i in range(len(self.columnas)+ 1):
            self.grid_columnconfigure(i, weight=1)
        
        #Variable para alamcenar datos a usar
        self.conteo = tk.IntVar(value=0)
        self.filters = {}
        
        #Etiquetas informativas
        ttk.Label(self, text='Registro de tickets', style="Titulo.TLabel").grid(row=0, column=5, columnspan=2, pady=20)
        ttk.Label(self, textvariable=self.contador, font=('Arial', 10)).grid(row=2, column=12, sticky='e')
        
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
        ttk.Button(self, text='Subir archivo', command= lambda: self.subir_archivo(self)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
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
        self.tabla.bind('<Motion>', self.on_hover)
        self.tabla.bind('<Leave>', self.on_leave)
        
        #Cargar datos en la tabla y actualizar conteo 
        mostrar_datos(query_datos(), self.tabla)
        self.conteo.set(mostrar_datos(query_datos(), self.tabla))
        self.contador.set(f"Se muestran: {self.conteo.get()}")
        
    #Llamar ventana para edición de datos
    def obtener_ticket(self, event):
        ticket = self.tabla.selection()[0]
        id_ticket = self.tabla.item(ticket, "values")[0]
        titulo_ticket = self.tabla.item(ticket, "values")[1]
        EditarTicket(self, id_ticket, titulo_ticket, self.tabla)
    
    #Llamar función  de filtro
    def filtrar(self, event):
        filter_values = {col: self.filters[col].get() for col in self.columnas}
        filtro(self.tabla, filter_values)
        self.conteo.set(mostrar_datos(filtro(self.tabla, filter_values), self.tabla))
        self.contador.set(f"Se muestran: {self.conteo.get()}")
    
    def subir_archivo(self, frame):
        reporte = cargar_datos(frame)
        progressbar = Progressbar(self)
        self.after(100, lambda: subir_tickets(self.tabla, self, reporte, progressbar))
        self.conteo.set(mostrar_datos(query_datos(), self.tabla))
        self.contador.set(f'Se muestran: {self.conteo.get()}')
    
    def traer_tabla(self):
        tabla = self.tabla
        return tabla

    def on_hover(self, event):
        item = self.tabla.identify_row(event.y)
        
        if self.last_hover and self.last_hover not in self.tabla.get_children():
            self.last_hover = None
        
        if item and item != self.last_hover:
            
            if self.last_hover:
                self.tabla.item(self.last_hover, tags=())
            
            self.tabla.tag_configure("hover", background="#D3D3D3", foreground="black")
            self.tabla.item(item, tags=("hover",))
            
            self.last_hover = item
    
    def on_leave(self, event):
        if self.last_hover and self.last_hover in self.tabla.get_children():
            self.tabla.item(self.last_hover, tags=())
        
        self.last_hover = None