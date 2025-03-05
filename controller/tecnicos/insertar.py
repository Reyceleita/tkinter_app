from tkinter import messagebox
import tkinter as tk

from controller.data.validaciones import *
from controller.data.obtener_data import *
from controller.tecnicos.consultar import *
from view.alertas.error import *
from view.alertas.warning import *
from logs.logger_config import logger

def crear_tecnico(cargo_id, cargo, fecha_ingreso, nombre, fecha_salida, tabla_tecnicos, nombre_c, fecha_i_c, fecha_s_c, cargo_c, frame):
    """
    Agrega un nuevo técnico a la base de datos
    
    Parámetros:
        cargo_id (dict): diccionario para los cargos
        cargo (ttk.Combobox): Valor del cargo
        fecha_ingreso (ttk.Entry): Valor de fecha de ingreso
        nombre (ttk.Entry): Valor de nombre
        fecha_salida (ttk.Entry): valor de fecha de salida
        tabla_tecnicos (ttk.TreeView): Tabla donde mostrar técicos
        nombre_c (ttk.Entry): Campo del formulario
        fecha_i_c (ttk.Entry): Campo del formulario
        fecha_s_c (ttk.Entry): Campo del formulario
        cargo_c (ttk.Combobox): Campo del formulario
    
    Resultados:
        Agrega un nuevo tecnico a la basae de datos o arroja algún error
    
    """
    existe = False
    command_b = "SELECT nombre FROM tecnicos"
    cursor.execute(command_b)
    tecnicos = cursor.fetchall()
    
    cargo = obtener_cargo(cargo_id, cargo)
    if validar_fecha(fecha_ingreso) and validar_fecha(fecha_salida):
        if nombre.strip() != "" and cargo is not None:
            nombre = str(nombre)
            fecha_ingreso = str(fecha_ingreso)
            fecha_salida = str(fecha_salida)
            
            for t in tecnicos:
                tecnico = str(t[0])
                tecnico = tecnico.lower()
                tecnico = tecnico.replace(" ","")
                nom = nombre.lower()
                nom = nom.replace(" ","")
                
                if tecnico == nom:
                    existe = True
            
            if existe:
                texto = 'El técnico ya existe'
                ErrorAlert(frame, texto)
            else:
                try:
                    command = """
                        INSERT INTO tecnicos (nombre, cargo_id, fecha_ingreso, fecha_salida)
                        VALUES (?,?,?,?)
                    """
                    cursor.execute(command, (nombre, cargo, fecha_ingreso, fecha_salida))
                    connection.commit()
                    cargar_tecnicos(tabla_tecnicos)
                    nombre_c.delete(0, tk.END)
                    fecha_i_c.delete(0, tk.END)
                    fecha_s_c.delete(0, tk.END)
                    cargo_c.delete(0, tk.END)
                except Exception as e:
                    logger.error('No se pudo crear el tecnico: %s', e)
                    ErrorAlert(frame, 'Error al crear el técnico')
        else:
            AdverteciaAlerta(frame, 'Complete todos los campos')
    else:
        AdverteciaAlerta(frame, 'Fecha inválida \nFormato correcto: YYYY-MM-DD')