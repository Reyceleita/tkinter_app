import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.data.borrar_datos import *
from controller.data.exportToSCV import *

#Vista para elminar base de datos local
class Datos():
    def __init__(self, frame):
        
        for widget in frame.winfo_children():
            widget.destroy()
        
        #Mostrar opciones
        ttk.Label(frame, text='Datos').grid(row=0, column=0, columnspan=2, sticky='we')
        ttk.Label(frame, text='Elimminar datos').grid(row=1, column=0, padx=5, sticky='w')
        ttk.Button(frame, text='Eliminar BD local', command=self.confrmar_eliminar).grid(row=2, column=0, pady=10, padx=20)
        ttk.Button(frame, text='Exportar a csv', command=lambda: exportar_datos(frame)).grid(row=3, column=0, pady=10, padx=20)
    
    
    def confrmar_eliminar(self):
        confirmar = tk.Toplevel()
        confirmar.wm_attributes("-topmost", True)
        confirmar.grid()
        
        ttk.Label(confirmar, text='¿Continuar con el borrado de datos?').grid(row=1, column=0, padx=10, pady=20)
        ttk.Button(confirmar, text='Cancelar', command=lambda: confirmar.destroy()).grid(row=2, column=0, padx=10, pady=10, sticky='e')
        ttk.Button(confirmar, text='Confirmar', command=lambda: eliminar_db(confirmar)).grid(row=2, column=1, padx=10, pady=10, sticky='w')
        
        confirmar.update_idletasks()
        confirmar.geometry("")
        ancho = confirmar.winfo_reqwidth()
        alto = confirmar.winfo_reqheight()
        x = (confirmar.winfo_screenwidth() // 2) - (ancho // 2)
        y = (confirmar.winfo_screenheight() // 2) - (alto // 2)
        confirmar.geometry(f"{ancho}x{alto}+{x}+{y}")
        confirmar.grab_set()