from tkinter import *
import tkinter as tk
from tkinter import ttk

from controller.data.obtener_data import *
from controller.tickets.actualizar import *

class EditarTicket(tk.Toplevel):
    def __init__(self, parent, id, nombre, tabla):
        super().__init__(parent)
        
        script_lista = {}
        tecnico_lista = {}
        solucion_lista = {}
        id_ticket = IntVar(value=id)
        self.titulo = StringVar(value=nombre)
        self.tecnico_db = StringVar()
        self.solucion_db = StringVar()
        self.script_db = StringVar()
        self.observacion_db = StringVar()
        self.fecha_db = StringVar()
        
        info_ticket = obtener_desplegables_tickets(id_ticket.get())

        self.tecnico_db.set(info_ticket[0])
        self.solucion_db.set(info_ticket[1])
        self.script_db.set(info_ticket[2])
        self.fecha_db.set(info_ticket[3])
        
        if self.fecha_db.get() == "None":
            self.fecha_db.set("Sin definir")
        
        ttk.Label(self, text='Editar', font=('Arial', 20)).grid(row=0, column=0, columnspan=3)
        ttk.Entry(self, textvariable=id_ticket, width=8, state='readonly').grid(row=1, column=0, pady=5, padx=5, sticky='w')
        ttk.Entry(self, textvariable=self.titulo, state='readonly').grid(row=1, column=0, columnspan=3, padx=65, sticky='we')
        ttk.Label(self, text='Técnio asignado', font=('Arial', 12)).grid(row=2, column=0, pady=5)
        tecnico = ttk.Combobox(self, textvariable=self.tecnico_db, state='readonly', width=30)
        tecnico.grid(row=3, column=0, pady=5, padx=40,)
        ttk.Label(self, text='Forma de solución', font=('Arial', 12)).grid(row=2, column=2, pady=5, padx=40, sticky='e')
        solucion = ttk.Combobox(self, textvariable=self.solucion_db, state='readonly', width=30)
        solucion.grid(row=3, column=2, pady=5, padx=40, sticky='e')
        ttk.Label(self, text='Observación', font=('Arial', 12)).grid(row=6, column=0, pady=5, padx=40,)
        observacion = tk.Entry(self, width=30, textvariable=self.observacion_db)
        observacion.grid(row=7, column=0, pady=5, padx=40, rowspan=2)
        ttk.Label(self, text='Script usado', font=('Arial', 12)).grid(row=4, column=0, pady=5, padx=40)
        script = ttk.Combobox(self, textvariable=self.script_db, state='readonly', width=30)
        script.grid(row=5, column=0, pady=5, padx=40)
        ttk.Label(self, text='Fecha de la solución', font=('Arial', 12)).grid(row=4, column=2, pady=5, padx=40, sticky='e')
        fecha = ttk.Entry(self, textvariable=self.fecha_db, width=33)
        fecha.grid(row=5, column=2, pady=5, padx=40, sticky='e')
        cargar_solucion(solucion, solucion_lista)
        cargar_script(script, script_lista)
        cargar_tecnico(tecnico, tecnico_lista)

        self.guardar = ttk.Button(self, text='Guardar', width=25, command=lambda: actualizar_ticket(id_ticket.get(), solucion.get(), tecnico.get(), script.get(), fecha.get(),
                                                                                            self.observacion_db.get(), self, tecnico_lista, script_lista, solucion_lista, tabla))
        
        self.guardar.grid(row=7, column=2, rowspan=2, pady=5, padx=40, sticky='e')