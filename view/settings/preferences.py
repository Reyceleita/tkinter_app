import tkinter as tk
from tkinter import *
from tkinter import ttk

from settings.settings import * 
from view.alertas.warning import *

#Canbiar el tema de la app
class Preferencias():
    def __init__(self, frame, p, parent):
        for widget in frame.winfo_children():
            widget.destroy()
        
        self.fra = p
        self.parent = parent
        self.temas = {
            'Tema oscuro': 'Dark_theme',
            'Tema claro': 'Light_theme',
            'Tema neon': 'Neon_theme',
            'Tema solar': 'Solarized_theme'
        }
        
        ttk.Label(frame, text='Preferencias').grid(row=0, column=0, columnspan=2, sticky='we')
        ttk.Label(frame, text='Tema: ').grid(row=1, column=0, padx=25, sticky='w')
        self.tema = ttk.Combobox(frame, values=('Tema oscuro', 'Tema claro', 'Tema neon', 'Tema solar'), state='readonly')
        self.tema.grid(row=2, column=0, padx=25)
        ttk.Button(frame, text='Aplicar', command=self.cambiar_tema).grid(row=3, column=1, sticky='w')
    
    def cambiar_tema(self):
        
        tema = self.tema.get()
        tema = self.temas.get(tema)
        if tema is None:
            AdverteciaAlerta(self.parent, 'De escoger un tema')
            return
        bg = ''
        fg = ''
        
        if tema == 'Dark_theme':
            bg = '#121212'
            fg = '#B0B0B0'
            
        elif tema == 'Light_theme':
            bg = '#F5F5F5'
            fg = '#0FF0FC'
        elif tema == 'Neon_theme':
            bg = '#101010'
            fg = '#B0B0B0'
        elif tema == 'Solarized_theme':
            bg = '#FDF6E3'
            fg = '#657B83'
        
        config = {
            "tema": tema,
            "background": bg,
            "foreground": fg
        }
        
        guardar_config(config)
        self.parent.aplicar_tema()
        self.fra.destroy()