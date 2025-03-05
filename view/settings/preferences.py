import tkinter as tk
from tkinter import *
from tkinter import ttk


#Canbiar el tema de la app
class Preferencias():
    def __init__(self, frame):
        
        for widget in frame.winfo_children():
            widget.destroy()
        
        ttk.Label(frame, text='Preferencias').grid(row=0, column=0, columnspan=2, sticky='we')
        ttk.Label(frame, text='Tema: ').grid(row=1, column=0, padx=25, sticky='w')
        ttk.Combobox(frame, values=('Dark_theme'), state='readonly'). grid(row=2, column=0, padx=25)
        ttk.Button(frame, text='Aplicar', command='').grid(row=3, column=1, sticky='w')