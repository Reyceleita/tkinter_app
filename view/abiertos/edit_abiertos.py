from tkinter import *
import tkinter as tk
from tkinter import ttk

from controller.data.obtener_data import *
from controller.abiertos.actualizar import *

class EditarAbiertos(tk.Toplevel):
    def __init__(self, parent, id, nombre, tabla):
        super().__init__(parent)
        
        solucion_list = {}
        tecnico_list = {}
        script_list = {}
        id_ticket = StringVar(value=id)
        self.titulo = StringVar(value=nombre)
        self.tecnico_db = StringVar()
        self.solucion_db = StringVar()
        self.script_db = StringVar()
        self.observacion_db = StringVar()
        self.fecha_db = StringVar()
        
        self.geometry('800x500')
        self.grid()
        self.columnconfigure(2, weight=1)
        self.rowconfigure(9, weight=1)
        
        info_ticket = obtener_desplegables(id_ticket.get())
        
        self.tecnico_db.set(info_ticket[0])
        self.solucion_db.set(info_ticket[1])
        self.script_db.set(info_ticket[2])
        self.fecha_db.set(info_ticket[3])
        
        
        if self.fecha_db.get() == 'None':
            self.fecha_db.set('Sin definir')
        
        ttk.Label(self, text='Editar', font=('Arial', 20)).grid(row=0, column=0, columnspan=3)
        ttk.Entry(self, textvariable=id_ticket, width=8, state='readonly').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(self, textvariable=self.titulo, state='readonly').grid(row=1, column=0, columnspan=3, padx=65, sticky='we')
        ttk.Label(self, text='Tecnoco asignado', font=('Arial', 12)).grid(row=2, column=0, pady=5)
        tecnico_campo = ttk.Combobox(self, textvariable=self.tecnico_db, state='readonly', width=30)
        tecnico_campo.grid(row=3, column=0, pady=5, padx=40)
        ttk.Label(self, text='Forma de solución', font=('Arial', 12)).grid(row=2, column=2, pady=5, padx=40)
        solucion_campo = ttk.Combobox(self, textvariable=self.solucion_db, state='readonly', width=30)
        solucion_campo.grid(row=3, column=2, pady=5, padx=40, sticky='e')
        ttk.Label(self, text='Observación', font=('Arial', 12)).grid(row=6, column=0, pady=5, padx=40)
        obsevacion_campo = ttk.Entry(self, width=30, textvariable=self.observacion_db)
        obsevacion_campo.grid(row=7, column=0, pady=5, padx=40, sticky='e')
        ttk.Label(self, text='Script usado', font=('Arial', 12)).grid(row=4, column=0, pady=5, padx=40, sticky='e')
        script_campo = ttk.Combobox(self, textvariable=self.script_db, state='readonly', width=30)
        script_campo.grid(row=5, column=0, pady=5, padx=40)
        ttk.Label(self, text='Fecha de solución', font=('Arial', 12)).grid(row=4, column=2, pady=5, padx=40, sticky='e')
        fecha_campo = ttk.Entry(self, textvariable=self.fecha_db, width=33)
        fecha_campo.grid(row=5, column=2, pady=5, padx=40, sticky='e')
        
        cargar_solucion(solucion_campo, solucion_list)
        cargar_script(script_campo, script_list)
        cargar_tecnico(tecnico_campo, tecnico_list)
        
        guardar = ttk.Button(self, text='Guardar', width=25, command= lambda: actualizar_abierto(id_ticket.get(), solucion_campo.get(), tecnico_campo.get(), script_campo.get(), fecha_campo.get(), 
                                                                                            obsevacion_campo.get(), self, tecnico_list, script_list, solucion_list, tabla))
        guardar.grid(row=7, column=2, rowspan=2, pady=5, padx=40, sticky='e')

