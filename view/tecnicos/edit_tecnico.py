import tkinter as tk
from tkinter import *
from tkinter import ttk

from model.connection import *
from controller.data.obtener_data import *
from controller.tecnicos.actualizar import *

#Ventana para editar un técnico
class EditarTecnico(tk.Toplevel):
    def __init__(self, parent, nombre, tabla_tecnicos, cargo_lista):
        super().__init__(parent)
        
        #Variables con información del técnico
        self.id_tecnico_db = StringVar()
        self.cargo_db = StringVar()
        self.nombre_tecnico_db = StringVar()
        self.ingreso_db = StringVar()
        self.salida_db = StringVar()
        self.cargo_id = {}

        #Obtener y asignar datos de técnico
        tecnico = tecnico_nobre(nombre)
        self.id_tecnico_db.set(tecnico[0])
        self.cargo_db.set(tecnico[1])
        self.ingreso_db.set(tecnico[2])
        self.salida_db.set(tecnico[3])
        self.nombre_tecnico_db.set(nombre)

        #Configuraciones de ventana
        self.geometry("355x250")
        self.grid()
        self.columnconfigure(2, weight=1)
        self.rowconfigure(5, weight=1)
        self.resizable(False, False)

        #Etiquetas informativas
        ttk.Label(self, text='Editar técnico', font=('Arial', 18)).grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(self, text='Nombre', font=('Arial',12)).grid(row=1, column=0, padx=25, pady=5, sticky='w')
        ttk.Label(self, text='Cargo', font=('Arial', 12)).grid(row=3, column=0, padx=25, pady=5, sticky='w')
        ttk.Label(self, text='Fecha de inicio', font=('Arial', 12)).grid(row=1, column=1, padx=25, pady=5, sticky='e')
        ttk.Label(self, text='Fecha de salida', font=('Arial', 12)).grid(row=3, column=1, padx=25, pady=5, sticky='e')
        
        #Campos de entrada
        self.cargo_campo = ttk.Combobox(self, state='readonly', textvariable=self.cargo_db, width=17)
        self.nombre_campo = ttk.Entry(self, textvariable=self.nombre_tecnico_db)
        self.fecha_i_campo = ttk.Entry(self, textvariable=self.ingreso_db)
        self.fecha_s_campo = ttk.Entry(self, textvariable=self.salida_db)
        
        #Posicionamiento de widgegts
        self.nombre_campo.grid(row=2, column=0, padx=25, pady=5)
        self.cargo_campo.grid(row=4, column=0, padx=25, pady=5)
        self.fecha_i_campo.grid(row=2, column=1, padx=25, pady=5, sticky='e')
        self.fecha_s_campo.grid(row=4, column=1, padx=25, pady=5, sticky='e')
        
        #Agregar ventana de confirmación.
        #Botón de acción
        ttk.Button(self, text='Guardar', command=lambda: actualizar_tecnico( self.id_tecnico_db.get(), self.cargo_campo.get(),
                                                                                self.fecha_i_campo.get(), self.fecha_s_campo.get(), 
                                                                                self.nombre_campo.get(), self, cargo_lista, 
                                                                                tabla_tecnicos)).grid(row=5, column=1, padx=25, pady=5, sticky='e')

        #Cargar datos en combobox
        cargar_cargo(self.cargo_id, self.cargo_campo)
        
        self.update_idletasks()
        self.geometry("")
        ancho = self.winfo_reqwidth()
        alto = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.grab_set()