import tkinter as tk
from tkinter import *
from tkinter import ttk

class Tecnicos():
    def __init__(self, frame):
        
        for widget in frame.winfo_children():
            widget.destroy()
        
        