import tkinter as tk
from tkinter import *
from tkinter import ttk

class ErrorAlert(tk.Toplevel):
    def __init__(self, parent, texto):
        super().__init__(parent)
        
        self.texto = StringVar()
        self.texto.set(texto)
        
        self.overrideredirect(True)
        self.geometry("250x100+600+250")
        self.wm_attributes("-topmost", True)
        self.grid()
    
        ttk.Label(self, text='Advertencia', style='Error.TLabel').grid(column=0, row=0, columnspan=2)
        ttk.Label(self, textvariable=self.texto).grid(column=0, row=1)
        ttk.Button(self, text='Cerrar', command=self.destroy).grid(column=1, row=2, sticky='e')