import tkinter as tk
from tkinter import *
from tkinter import ttk

class Completado(tk.Toplevel):
    def __init__(self, parent, texto):
        super().__init__(parent)
        
        self.texto = StringVar()
        self.texto.set(texto)
        
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)
        self.grid()
        self.configure(bg='#A0A0A0', bd=10, relief='raised')
        x = (parent.winfo_screenwidth() - 315) // 2
        y = (parent.winfo_screenheight() - 120) // 2
        self.geometry(f"{315}x{120}+{x}+{y}")
        self.grab_set()
    
        ttk.Label(self, text='Completado', style='Completado.TLabel').grid(column=0, row=0, columnspan=2)
        ttk.Label(self, textvariable=self.texto, style="TextCompletado.TLabel").grid(column=0, row=1)
        ttk.Button(self, text='Aceptar', command=self.destroy).grid(column=0, row=2, pady=5, sticky='e')