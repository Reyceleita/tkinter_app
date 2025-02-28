from tkinter import *
from tkinter import ttk
import tkinter as tk

from model.execution import *
from view.abiertos.abiertos import *
from view.tickets.tickets import *
from view.tecnicos.tecnicos import *
from view.styles.dark_mode import *


#HACERRR
#
#Mejorar UI 
#Completar y verificar estilos
#Crear Readme
#Arreglar conteo de tickets para alertas .¿
#Revisar para comentar
#Manejo de errores
#Buscar cómo convertirlo en app .¿
#
#Revisar que al subir reporte mensual no sobreescriba los revisados (creo q si valida ._.) >:/ (Revisar lógica actualizar abierto, [no actualiza si el cambio es sin cambios X.X])
#
#.¿


#Se crea app principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        style = ttk.Style()
        dark_theme(style)
        self.option_add("*background", "#121212")
        self.option_add("*foreground", "#B0B0B0")
        
        #Configura ventana principal
        self.title('App')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}-1+0")
        
        #Cear manejo de pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky='nswe')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        #Iniciar y agregan pestañas
        self.abiertos = TabAbiertos(self.notebook)
        self.tickets = TabTickets(self.notebook)
        self.tecnicos = TabTecnicos(self.notebook)
        
        self.notebook.add(self.abiertos, text='Abiertos')
        self.notebook.add(self.tecnicos, text='Tecnicos')
        self.notebook.add(self.tickets, text='Tickets')
        
        #Vincular evento de pestañas 
        
        self.notebook.bind('<<NotebookTabChanged>>', self.on_tab_selected)
        
    #Cargar datos al cambiar de pestaña
    def on_tab_selected(self, event):
        pestaña = self.notebook.index(self.notebook.select())
        
        if pestaña == 0:
            pass
        elif pestaña == 1:
            pass
        else:
            pass
    


#Ejecución de aplicación
if __name__ == '__main__':
    first_execute()
    app = App()
    app.mainloop()
    