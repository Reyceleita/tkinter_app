from tkinter import *
from tkinter import ttk

from controller.data.mostrar import *
from controller.data.obtener_data import *
from controller.tecnicos.insertar import *
from view.tecnicos.edit_tecnico import *
from view.tecnicos.agregar_tecnico import *

# Pestaña para el manejo de técnicos
class TabTecnicos(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configuración de la pestaña
        self.columnconfigure(3, weight=1)
        self.rowconfigure(3)

        # Variables para almacenar información de técnicos
        self.cargo_id = {}
        self.nombre = StringVar()
        self.fecha_ingreso = StringVar()
        self.fecha_salida = StringVar()
        self.last_hover = None

        # Columnas para la tabla
        columnas = (
            "Nombre",
            "Cargo",
            "Fecha de ingreso",
            "Fecha de salida",
            "Tickets asignados",
            "Tickets cerrados",
            "Estado",
        )

        # Configuración de tabla y scrollbar
        scrolly = ttk.Scrollbar(self, orient="vertical")
        self.tabla_tecnicos = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            yscrollcommand=scrolly,
            selectmode="browse",
        )
        
        ttk.Label(self, text="Tecnicos", font=("Arial", 14)).grid(
            row=0, column=0, columnspan=1, pady=5, padx=250, sticky="e"
        )

        # Posicionamiento de widgets en la interfaz
        self.tabla_tecnicos.grid(
            row=1, column=0, columnspan=1, rowspan=5, sticky="E", padx=17
        )
        scrolly.grid(row=1, column=0, rowspan=5, sticky="nse")
        scrolly.config(command=self.tabla_tecnicos.yview)

        # Configuración de encabezados de columna
        for columna in columnas:
            self.tabla_tecnicos.heading(
                columna,
                text=columna,
                command=lambda c=columna: ordenar_tabla(
                    self.tabla_tecnicos, c, False, columnas
                ),
            )
            self.tabla_tecnicos.column(columna, width=100)

        # Vincular selección de la tabla a una función
        self.tabla_tecnicos.bind("<<TreeviewSelect>>", self.obtener_tecnico)
        self.tabla_tecnicos.bind("<Motion>", self.on_hover)
        self.tabla_tecnicos.bind("<Leave>", self.on_leave)

        # Cargar datos en la taba
        cargar_tecnicos(self.tabla_tecnicos)
        
        #Botón de acción
        ttk.Button(self, text='Crear', command=lambda: AgregarTecnico(self, self.tabla_tecnicos)).grid(column=0, row=6, pady=5, sticky='e')

    # Crear ventana de edición según selección en la tabla
    def obtener_tecnico(self, event):
        tecnico = self.tabla_tecnicos.selection()[0]
        nombre = str(self.tabla_tecnicos.item(tecnico, "values")[0])
        EditarTecnico(self, nombre, self.tabla_tecnicos, self.cargo_id)

    # Guardar tabla en variable para usar
    def traer_tabla(self):
        tabla = self.tabla_tecnicos
        return tabla

    # Manejar hover (resalto) para la tabla
    def on_hover(self, event):
        item = self.tabla_tecnicos.identify_row(event.y)
        if item and item != self.last_hover:

            if self.last_hover:
                self.tabla_tecnicos.item(self.last_hover, tags=())

            self.tabla_tecnicos.tag_configure(
                "hover", background="#D3D3D3", foreground="black"
            )
            self.tabla_tecnicos.item(item, tags=("hover",))

            self.last_hover = item

    def on_leave(self, event):
        if self.last_hover:
            self.tabla_tecnicos.item(self.last_hover, tags=())
            self.last_hover = None
