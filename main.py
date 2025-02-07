from tkinter import *
from tkinter import ttk
import tkinter as tk
import ctypes

from model.execution import *
from view.abiertos.abiertos import *
from view.styles.dark_mode import *

#
#
#


#Se crea app principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        style = ttk.Style()
        dark_theme(style)
        self.option_add("*background", "#121212")
        self.option_add("*foreground", "#B0B0B0")
        
        # Oculta la barra de título por defecto
        #self.overrideredirect(True)  
        
        
        #Se cambia titulo y tamaño
        self.title('App')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}-1+0")
        
        self.hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
        
        
        #Se crea notebook para manejo de pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky='nswe')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        #Se crean y agregan pestañas
        self.abiertos = TabAbiertos(self.notebook)
        #self.tickets = TabTickets(self.notebook)
        #self.tecnicos = TabTecnicos(self.notebook)
        
        self.notebook.add(self.abiertos, text='Abiertos')
        #self.notebook.add(self.tecnicos, text='Tecnicos')
        #self.notebook.add(self.tickets, text='Tickets')
        
        #Se vincula evento de pestañas a función
        
        self.notebook.bind('<<NotebookTabChanged>>', self.on_tab_selected)
        
    #Función para cargar datos al cambiar de pentaña
    def on_tab_selected(self, event):
        pestaña = self.notebook.index(self.notebook.select())
        
        if pestaña == 0:
            pass
        elif pestaña == 1:
            pass
        else:
            pass
    

first_execute()

if __name__ == '__main__':
    app = App()
    app.mainloop()