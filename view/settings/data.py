import tkinter as tk
from tkinter import *
from tkinter import ttk

from controller.data.borrar_datos import *
from controller.data.exportToSCV import *
from view.settings.update_data import *
from view.settings.insert_data import *
from view.settings.delete_data import *


# Vista para opciones de datos
class Datos(ttk.Frame):
    def __init__(self, parent, main):
        super().__init__(parent)

        # Mostrar frame
        self.grid(row=0, column=0, sticky="nswe")
        self.columnconfigure(2, weight=1)
        self.rowconfigure(8, weight=1)

        # Dividir frame principal para agregar información
        self.opciones = ttk.Frame(self)
        self.opciones.grid(row=0, column=0)
        self.opciones.rowconfigure(5, weight=1)
        self.contenido = ttk.Frame(self)
        self.contenido.grid(row=0, column=1)
        self.contenido.rowconfigure(5, weight=1)

        # Mostrar opciones
        ttk.Button(
            self.opciones,
            text="Agregar datos",
            command=lambda: InsertData(self.contenido),
        ).grid(row=4, column=0, padx=20, pady=10)
        ttk.Button(
            self.opciones,
            text="Modificar Datos",
            command=lambda: UpdateTablas(self.contenido),
        ).grid(row=5, column=0, padx=20, pady=10)
        ttk.Button(
            self.opciones,
            text="Eliinar un dato",
            command=lambda: DeleteData(self.contenido),
        ).grid(row=6, column=0, padx=20, pady=10)
        ttk.Button(
            self.opciones, text="Eliminar BD local", command=self.confrmar_eliminar
        ).grid(row=9, column=0, padx=20, pady=10)
        ttk.Button(
            self.opciones, text="Exportar a csv", command=lambda: exportar_datos(self)
        ).grid(row=10, column=0, padx=20, pady=10)

        ttk.Separator(self.opciones, orient="horizontal").grid(
            row=8, column=0, columnspan=2, padx=5, sticky="swe"
        )
        ttk.Separator(self, orient="vertical").grid(
            row=0, column=1, rowspan=10, sticky="wns"
        )
        ttk.Button(self.opciones, text="Regresar", style='Adv.TButton', command=main.destroy).grid(
            row=11, column=0, padx=20, pady=20
        )

    # Confirmación para eliminar datos locales y llamado de función
    def confrmar_eliminar(self):
        # Se crea alerta
        confirmar = tk.Toplevel()
        confirmar.wm_attributes("-topmost", True)
        confirmar.grid()

        # Widgets de información
        ttk.Label(confirmar, text="¿Continuar con el borrado de datos?").grid(
            row=1, column=0, padx=10, pady=20
        )
        ttk.Button(
            confirmar, text="Cancelar", command=lambda: confirmar.destroy()
        ).grid(row=2, column=0, padx=10, pady=10, sticky="e")

        # Botón de confirmación
        ttk.Button(
            confirmar, text="Confirmar", command=lambda: eliminar_db(confirmar)
        ).grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Configuración de alerta
        confirmar.update_idletasks()
        confirmar.geometry("")
        ancho = confirmar.winfo_reqwidth()
        alto = confirmar.winfo_reqheight()
        x = (confirmar.winfo_screenwidth() // 2) - (ancho // 2)
        y = (confirmar.winfo_screenheight() // 2) - (alto // 2)
        confirmar.geometry(f"{ancho}x{alto}+{x}+{y}")
        confirmar.grab_set()
