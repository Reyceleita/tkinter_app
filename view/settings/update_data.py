from tkinter import *
from tkinter import ttk

from controller.data.obtener_data import *
from controller.BD.update import *
from view.alertas.warning import *

# Vista para actualizar datos de algunas tablas
class UpdateTablas:
    def __init__(self, frame):
        self.campo_list = {}
        self.fra = frame
        self.tablas = {
            "Cargos": "cargos",
            "Scripts": "scripts",
            "Forma de solución": "forma_solucion",
            '':''
        }

        # Limpiar frame para agregar los eiddgets
        for widget in frame.winfo_children():
            widget.destroy()

        # Widgets de informacion
        ttk.Label(frame, text="Modificar datos").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Tabla:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Registro a modificar:").grid(
            row=1, column=1, padx=10, pady=10
        )
        ttk.Label(frame, text="Nuevo valor:").grid(row=3, column=0, padx=10, pady=10)

        # Widgets para la actualizacion
        self.tabla = ttk.Combobox(
            frame, values=("Cargos", "Scripts", "Forma de solución"), state="readonly"
        )
        self.campo = ttk.Combobox(frame, values="", state="readonly")
        self.nuevo = ttk.Entry(frame)

        # Botón de accion
        ttk.Button(frame, text="Actualizar", command=self.actualiza).grid(
            row=4, column=3, padx=10, pady=10
        )

        # Mostrar widgets
        self.nuevo.grid(row=4, column=0, padx=10, pady=10)
        self.tabla.grid(row=2, column=0, padx=10, pady=10)
        self.campo.grid(row=2, column=1, padx=10, pady=10)
        self.tabla.bind("<<ComboboxSelected>>", self.cargar_datos)

    # Agregar a desplegables los datos correspondientes
    def cargar_datos(self, event):

        tabla = self.tabla.get()

        tabla = self.tablas.get(tabla)

        cargar_tablas(self.campo, self.campo_list, tabla)

    # Llamar función para actualizar según parámetros
    def actualiza(self):

        tabla = self.tabla.get()
        tabla = self.tablas.get(tabla)
        nombre = self.nuevo.get()
        combobox = self.campo.get()
        if tabla == '' or combobox == '':
            AdverteciaAlerta(self.fra, 'Debes completar los todos los campos')
        id = obtener_campo_lista(self.campo_list, combobox)
        if tabla == "cargos":
            campo = "cargo"
            valor = "id_cargo"
        elif tabla == "scripts":
            campo = "script"
            valor = "id_script"
        elif tabla == "forma_solucion":
            campo = "solucion"
            valor = "id_solucion"
        update_valor(self.fra, id, nombre, tabla, campo, valor)
