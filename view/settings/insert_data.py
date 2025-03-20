import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.data.obtener_data import *
from controller.BD.insert import *


# Vista para agregar un nuevo dato a alguna tabla
class InsertData:
    def __init__(self, frame):
        self.campo_list = {}
        self.fra = frame

        # Vista para actualizar datos de algunas tablas
        for widget in frame.winfo_children():
            widget.destroy()

        # Tablas en las que se puede actualizar
        self.tablas = {
            "Cargos": "cargos",
            "Scripts": "scripts",
            "Forma de solución": "forma_solucion",
        }

        # Widgets de información
        ttk.Label(frame, text="Agregar datos").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Tabla:").grid(row=1, column=0, padx=10, pady=10)

        # Widgets de ingreso de datos
        self.tabla = ttk.Combobox(
            frame, values=("Cargos", "Scripts", "Forma de solución"), state="readonly"
        )
        self.nuevo = tk.Entry(frame)

        # Botón de acciónn
        ttk.Button(frame, text="Agregar", command=self.agregar).grid(
            row=4, column=3, padx=10, pady=10
        )

        # Mostrar widgets
        self.nuevo.grid(row=4, column=0, padx=10, pady=10)
        self.tabla.grid(row=2, column=0, padx=10, pady=10)
        self.tabla.bind(
            "<<ComboboxSelected>>",
        )

    # Llamar función de inserción sesgún parámetros
    def agregar(self):
        tabla = self.tabla.get()
        tabla = self.tablas.get(tabla)
        nombre = self.nuevo.get()
        if tabla == "cargos":
            campo = "cargo"
        elif tabla == "scripts":
            campo = "script"
        elif tabla == "forma_solucion":
            campo = "solucion"
        insert(self.fra, nombre, tabla, campo)
