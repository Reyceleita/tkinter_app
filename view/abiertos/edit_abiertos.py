from tkinter import *
import tkinter as tk
from tkinter import ttk

from controller.data.obtener_data import *
from controller.abiertos.actualizar import *


# Ventana para editar un ticket abierto
class EditarAbiertos(tk.Toplevel):
    def __init__(self, parent, id, nombre, tabla):
        super().__init__(parent)

        # Variables para información del ticket
        solucion_list = {}
        tecnico_list = {}
        script_list = {}
        id_ticket = StringVar(value=id)
        self.titulo = StringVar(value=nombre)
        self.tecnico_db = StringVar()
        self.solucion_db = StringVar()
        self.script_db = StringVar()
        self.observacion_db = StringVar()
        self.fecha_db = StringVar()

        # Conficuración de ventana para editar
        self.geometry("800x500")
        self.grid()
        self.columnconfigure(2, weight=1)
        self.rowconfigure(9, weight=1)

        # Obtener y asignar datos del ticket
        info_ticket = obtener_desplegables(id_ticket.get())
        self.tecnico_db.set(info_ticket[0])
        self.solucion_db.set(info_ticket[1])
        self.script_db.set(info_ticket[2])
        self.fecha_db.set(info_ticket[3])
        self.observacion_db.set(
            cargar_observacion("tickets_diarios", id_ticket.get())
        )  # Cargar observación guardada en BD
        if self.fecha_db.get() == "None":
            self.fecha_db.set("Sin definir")

        # Estiquetas de información
        ttk.Label(self, text="Editar", font=("Arial", 20)).grid(
            row=0, column=0, columnspan=3
        )
        ttk.Label(self, text="Tecnico asignado", font=("Arial", 12)).grid(
            row=2, column=0, pady=5
        )
        ttk.Label(self, text="Forma de solución", font=("Arial", 12)).grid(
            row=2, column=1, pady=5, padx=40
        )
        ttk.Label(self, text="Observación", font=("Arial", 12)).grid(
            row=6, column=0, pady=5, padx=40
        )
        ttk.Label(self, text="Script usado", font=("Arial", 12)).grid(
            row=4, column=0, pady=5, padx=40
        )
        ttk.Label(self, text="Fecha de solución", font=("Arial", 12)).grid(
            row=4, column=1, pady=5, padx=40
        )

        # Campos de entrada
        ttk.Entry(
            self, textvariable=self.titulo, state="readonly", style="Label.TEntry"
        ).grid(row=1, column=0, columnspan=3, padx=65, sticky="we")
        ttk.Entry(
            self,
            textvariable=id_ticket,
            width=8,
            state="readonly",
            style="Label.TEntry",
        ).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        obsevacion_campo = ttk.Entry(
            self, width=30, textvariable=self.observacion_db)
        fecha_campo = ttk.Entry(self, textvariable=self.fecha_db, width=33)
        tecnico_campo = ttk.Combobox(
            self, textvariable=self.tecnico_db, state="readonly", width=30
        )
        solucion_campo = ttk.Combobox(
            self, textvariable=self.solucion_db, state="readonly", width=30
        )
        script_campo = ttk.Combobox(
            self, textvariable=self.script_db, state="readonly", width=30
        )

        # Posicionamiento de widgets
        tecnico_campo.grid(row=3, column=0, pady=5, padx=40)
        solucion_campo.grid(row=3, column=1, pady=5, padx=40, sticky="e")
        obsevacion_campo.grid(
            row=7, column=0, columnspan=3, pady=5, padx=40, sticky="we"
        )
        script_campo.grid(row=5, column=0, pady=5, padx=40)
        fecha_campo.grid(row=5, column=1, pady=5, padx=40, sticky="e")

        # Cargar datos en combobox
        cargar_solucion(solucion_campo, solucion_list)
        cargar_script(script_campo, script_list)
        cargar_tecnico(tecnico_campo, tecnico_list)

        # Botón de acción
        guardar = ttk.Button(
            self,
            text="Guardar",
            width=15,
            style='Scf.TButton',
            command=lambda: actualizar_abierto(
                id_ticket.get(),
                solucion_campo.get(),
                tecnico_campo.get(),
                script_campo.get(),
                fecha_campo.get(),
                obsevacion_campo.get(),
                self,
                tecnico_list,
                script_list,
                solucion_list,
                tabla,
            ),
        )
        guardar.grid(
            row=8, column=1, pady=15, padx=40, sticky="w"
        )  # Posicionamiento de botón

        ttk.Button(
            self, text="Cancelar", width=15, style="Adv.TButton", command=self.destroy
        ).grid(row=8, column=0, pady=15, padx=20, sticky="e")

        # Definir dimensiones de la alerta
        self.update_idletasks()
        self.geometry("")
        ancho = self.winfo_reqwidth()
        alto = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.grab_set()
