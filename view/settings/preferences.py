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
        
        #Frames padres
        self.fra = p
        self.parent = parent
        
        #Lista de temas
        self.temas = {
            'Tema oscuro': 'Dark_theme',
            'Tema claro': 'Light_theme',
            'Tema neon': 'Neon_theme',
            'Tema solar': 'Solarized_theme'
        }
        
        #Widgets
        ttk.Label(frame, text='Preferencias').grid(row=0, column=0, columnspan=2, sticky='we')
        ttk.Label(frame, text='Tema: ').grid(row=1, column=0, padx=25, sticky='w')
        self.tema = ttk.Combobox(frame, values=('Tema oscuro', 'Tema claro', 'Tema neon', 'Tema solar'), state='readonly')
        self.tema.grid(row=2, column=0, padx=25)
        ttk.Button(frame, text='Aplicar', command=self.cambiar_tema).grid(row=3, column=1, sticky='w')
    
    #Función para guardar y aplicar un tema
    def cambiar_tema(self):
        
        tema = self.tema.get()
        tema = self.temas.get(tema)
        if tema is None:
            AdverteciaAlerta(self.parent, 'Debe escoger un tema')
            return
        bg = ''
        fg = ''
        list_bg = ''
        list_fg = ''
#-----------------------------------aaaaaaaaaa-----------------------------------#
        if tema == 'Dark_theme':
            bg = '#121212'
            fg = '#B0B0B0'
            list_bg = '#121212'
            list_fg = '#B0B0B0'
        elif tema == 'Light_theme':
            bg = '#F5F5F5'
            fg = '#333333'
            list_bg = '#F5F5F5'
            list_fg = '#333333'
        elif tema == 'Neon_theme':
            bg = '#101010'
            fg = '#B0B0B0'
            list_bg = '#101010'
            list_fg = '#B0B0B0'
        elif tema == 'Solarized_theme':
            bg = '#FDF6E3'
            fg = '#657B83'
            list_bg = '#FDF6E3'
            list_fg = '#657B83'
        
        config = {
            "tema": tema,
            "background": bg,
            "foreground": fg,
            "listbg": list_bg,
            "listfg": list_fg
        }
        
        guardar_config(config)
        self.parent.aplicar_tema()
        self.fra.destroy()