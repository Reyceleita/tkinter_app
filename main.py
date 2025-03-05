from tkinter import *
from tkinter import ttk
import tkinter as tk

from model.execution import *
from view.abiertos.abiertos import *
from view.tickets.tickets import *
from view.tecnicos.tecnicos import *
from view.styles.dark_mode import *
from settings.settings import *

#HACERRR
#
#Mejorar UI 
#Completar y verificar estilos
#Crear Readme
#Arreglar conteo de tickets para {alertas} .¿ /*ARREGLADO*/
#Revisar para comentar/*pro gre so*/
#Agregar hover para tablas /*LISTOOO*/
#Manejo de errores y agregar logs? /*LISTOOO*/
#Agregar confirmación en según que partes
#Buscar cómo convertirlo en app .¿
#Revisar que al subir reporte mensual no sobreescriba los revisados (creo q si valida ._.) >:/ (Revisar lógica actualizar abierto, [no actualiza si el cambio es sin cambios X_X]) /*ARREGLADOOOOOO*/
#
#Mejorar colores y agregar imágenes en alertas :P
#Crear más temas >:O
#
#Agregar pestaña para manejo de datos/*pro gre so*/
#Agregar lógica para vaciar tablas de DB 
#Organizar fechas 
#
#
#Cambiar nombre de app
#
# .¿


#Se crea app principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #Asignar estilos
        style = ttk.Style()
        dark_theme(style)
        
        aplicar_tema(style, self)
        
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
        
        #ttk.Button(self.notebook, text='*').place(x=1280, y=25)
        
    #Cargar datos al cambiar de pestaña
    def on_tab_selected(self, event):
        pestaña = self.notebook.index(self.notebook.select())
        
        if pestaña == 0:
            mostrar_datos(query_datos_activos(), self.abiertos.traer_tabla())
        elif pestaña == 1:
            cargar_tecnicos(self.tecnicos.traer_tabla())
        elif pestaña == 2:
            mostrar_datos(query_datos(), self.tickets.traer_tabla())

#Ejecución de aplicación
if __name__ == '__main__':
    first_execute()
    app = App()
    app.mainloop()
    