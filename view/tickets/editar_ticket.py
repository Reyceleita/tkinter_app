from tkinter import *
import tkinter as tk
from tkinter import ttk

from controller.data.obtener_data import *
from controller.tickets.actualizar import *
from controller.data.cargar_datos import *

# Ventana de edición para tickets


class EditarTicket(tk.Toplevel):
    def __init__(self, parent, id, nombre, tabla):
        super().__init__(parent)

        # Configuración de ventana
        self.geometry("800x500")
        self.columnconfigure(2, weight=1)
        self.rowconfigure(9, weight=1)

        # Variables para información del ticket
        script_lista = {}
        tecnico_lista = {}
        solucion_lista = {}
        id_ticket = IntVar(value=id)
        self.titulo = StringVar(value=nombre)
        self.tecnico_db = StringVar()
        self.solucion_db = StringVar()
        self.script_db = StringVar()
        self.observacion_db = StringVar()
        self.fecha_db = StringVar()

        # Asignación de valores a variables
        info_ticket = obtener_desplegables_tickets(id_ticket.get())
        self.tecnico_db.set(info_ticket[0])
        self.solucion_db.set(info_ticket[1])
        self.script_db.set(info_ticket[2])
        self.fecha_db.set(info_ticket[3])
        self.observacion_db.set(cargar_observacion("tickets", id_ticket.get()))
        if self.fecha_db.get() == "None":
            self.fecha_db.set("Sin definir")

        # Etiquetas informativas
        ttk.Label(self, text="Editar", font=("Arial", 20)).grid(
            row=0, column=0, columnspan=3
        )
        ttk.Label(self, text="Técnio asignado", font=("Arial", 12)).grid(
            row=2, column=0, pady=5
        )
        ttk.Label(self, text="Forma de solución", font=("Arial", 12)).grid(
            row=2, column=2, pady=5, padx=40, sticky="e"
        )
        ttk.Label(self, text="Observación", font=("Arial", 12)).grid(
            row=6,
            column=0,
            pady=5,
            padx=40,
        )
        ttk.Label(self, text="Script usado", font=("Arial", 12)).grid(
            row=4, column=0, pady=5, padx=40
        )
        ttk.Label(self, text="Fecha de la solución", font=("Arial", 12)).grid(
            row=4, column=2, pady=5, padx=40, sticky="e"
        )

        # Campos de entrada
        ttk.Entry(
            self,
            textvariable=id_ticket,
            width=8,
            state="readonly",
            style="Label.TEntry",
        ).grid(row=1, column=0, pady=5, padx=5, sticky="w")
        ttk.Entry(
            self, textvariable=self.titulo, state="readonly", style="Label.TEntry"
        ).grid(row=1, column=0, columnspan=3, padx=65, sticky="we")
        tecnico = ttk.Combobox(
            self, textvariable=self.tecnico_db, state="readonly", width=30
        )
        solucion = ttk.Combobox(
            self, textvariable=self.solucion_db, state="readonly", width=30
        )
        observacion = ttk.Entry(self, width=30, textvariable=self.observacion_db)
        script = ttk.Combobox(
            self, textvariable=self.script_db, state="readonly", width=30
        )
        fecha = ttk.Entry(self, textvariable=self.fecha_db, width=33)

        # Posicionamiento de widgets en la interfaz
        tecnico.grid(row=3, column=0, pady=5, padx=40)
        solucion.grid(row=3, column=2, pady=5, padx=40, sticky="e")
        observacion.grid(row=7, column=0, pady=5, padx=40, columnspan=3, sticky="we")
        script.grid(row=5, column=0, pady=5, padx=40)
        fecha.grid(row=5, column=2, pady=5, padx=40, sticky="e")

        # Alimentar combobox con su información
        cargar_solucion(solucion, solucion_lista)
        cargar_script(script, script_lista)
        cargar_tecnico(tecnico, tecnico_lista)

        # Botón de acción
        self.guardar = ttk.Button(
            self,
            text="Guardar",
            width=25,
            command=lambda: actualizar_ticket(
                id_ticket.get(),
                solucion.get(),
                tecnico.get(),
                script.get(),
                fecha.get(),
                self.observacion_db.get(),
                self,
                tecnico_lista,
                script_lista,
                solucion_lista,
                tabla,
            ),
        )
        self.guardar.grid(
            row=8, column=2, rowspan=2, pady=25, padx=40, sticky="e"
        )  # Posicionamiento del botón

        # Ajustes de ventana
        self.update_idletasks()
        self.geometry("")
        ancho = self.winfo_reqwidth()
        alto = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.grab_set()
