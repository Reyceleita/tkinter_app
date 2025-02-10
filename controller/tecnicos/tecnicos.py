import tkinter as tk 
from tkinter import *
from tkinter import ttk



class TabTicket(ttk.Frame):
    def __init(self , parent):
        super().__init__(parent)
        
        cargo_id = {}
        self.columnconfigure(3, weight=1)
        self.rowconfigure(3)
        
        nombre = StringVar()
        fecha_saidad = StringVar()
        fecha_salida = StringVar()
        
        ttk.Label(self, text='Registrar técnico').grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(self, text='Nombre:').grid(row=1, column=0, columnspan=1, padx=20, pady=5, sticky='w' )