from tkinter import *
from tkinter import ttk

from controller.data.mostrar import *
from controller.data.obtener_data import *
from controller.tecnicos.insertar import *
from view.tecnicos.edit_tecnico import *


class AgregarTecnico(tk.Toplevel):
    def __init__(self, parent, tabla):
        super().__init__(parent)
        
        self.wm_attributes("-topmost", True)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2)
        self.title('Crear técnico')
        
        # Variables para almacenar información de técnicos
        self.cargo_id = {}
        self.nombre = StringVar()
        self.fecha_ingreso = StringVar()
        self.fecha_salida = StringVar()
        self.last_hover = None
        
        # etiquetas informativas
        ttk.Label(self, text="Registrar técnico").grid(
            row=0, column=1, columnspan=2, pady=5, sticky='w'
        )
        ttk.Label(self, text="Nombre:").grid(
            row=1, column=0, columnspan=1, padx=20, pady=5, sticky="w"
        )
        ttk.Label(self, text="Cargo:", font=("Arial", 10)).grid(
            row=2, column=0, columnspan=1, padx=20, pady=5, sticky="w"
        )
        ttk.Label(self, text="Fecha de ingreso:", font=("Arial", 10)).grid(
            row=3, column=0, columnspan=1, padx=20, pady=5, sticky="w"
        )
        ttk.Label(self, text="Fecha de salida:", font=("Arial", 10)).grid(
            row=4, column=0, columnspan=1, padx=20, pady=5, sticky="w"
        )
        
        # Campos de entrada
        self.cargo_campo = ttk.Combobox(self, state="readonly", font=("Arila", 9), width=23)
        self.nombre_campo = ttk.Entry(
            self, font=("Arial", 9), width=23, textvariable=self.nombre
        )
        self.ingreso_campo = ttk.Entry(
            self, width=23, font=("Arial", 9), textvariable=self.fecha_ingreso
        )
        self.salida_campo = ttk.Entry(
            self, width=23, font=("Arial", 9), textvariable=self.fecha_salida
        )
        
        # Posicionamiento de widgets en la interfaz
        self.nombre_campo.grid(row=1, column=1, columnspan=2, pady=5, padx=30, sticky="w")
        self.cargo_campo.grid(row=2, column=1, pady=5, padx=30, columnspan=2)
        self.ingreso_campo.grid(row=3, column=1, columnspan=2, pady=5, padx=30, sticky="w")
        self.salida_campo.grid(row=4, column=1, columnspan=2, pady=5, padx=30, sticky="w")
        
        #Agregar datos en combobx
        cargar_cargo(self.cargo_id, self.cargo_campo)
        
        
        # Botón de acción
        ttk.Button(
            self,
            text="Crear",
            width=10,
            command=lambda: crear_tecnico(
                self.cargo_id,
                self.cargo_campo.get(),
                self.ingreso_campo.get(),
                self.nombre_campo.get(),
                self.salida_campo.get(),
                tabla,
                self.nombre_campo,
                self.ingreso_campo,
                self.salida_campo,
                self.cargo_campo,
                self,
            ),
        ).grid(row=5, column=2, columnspan=1, padx=30, pady=15, sticky="e")
        
                # Configuracion finan de ventana
        self.wm_attributes("-topmost", True)
        self.update_idletasks()
        self.geometry("")
        ancho = self.winfo_reqwidth()
        alto = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.grab_set()