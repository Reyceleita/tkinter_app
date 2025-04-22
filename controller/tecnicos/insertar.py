import tkinter as tk

from controller.data.validaciones import *
from controller.data.obtener_data import *
from controller.tecnicos.consultar import *
from view.alertas.error import *
from view.alertas.warning import *
from logs.logger_config import logger

# Crear un técnico
def crear_tecnico(
    cargo_id,
    cargo,
    fecha_ingreso,
    nombre,
    fecha_salida,
    tabla_tecnicos,
    nombre_c,
    fecha_i_c,
    fecha_s_c,
    cargo_c,
    frame,
):

    # Conexión a base de dadtos
    connection = connection_to_db()
    cursor = connection.cursor()

    # Obtener tecnicos exitentes para validar
    existe = False  # Variable para validar
    command_b = "SELECT nombre FROM tecnicos"
    cursor.execute(command_b)
    tecnicos = cursor.fetchall()

    cargo = obtener_cargo(cargo_id, cargo)

    # Validar fechas para la creación
    if validar_fecha(fecha_ingreso) and validar_fecha(fecha_salida):
        # Validación de datos completos
        if nombre.strip() != "" and cargo is not None:

            # Asignación de valores a variables
            nombre = str(nombre)
            fecha_ingreso = str(fecha_ingreso)
            fecha_salida = str(fecha_salida)

            # Comparar le nombre del tecnico con los de la base de datos
            for t in tecnicos:
                tecnico = str(t[0])
                tecnico = tecnico.lower()
                tecnico = tecnico.replace(" ", "")
                nom = nombre.lower()
                nom = nom.replace(" ", "")

                if tecnico == nom:
                    existe = True
                    break

            if existe:
                # Mostrar ventana de alerta cuando ya exista el nombre
                texto = "El técnico ya existe"
                ErrorAlert(frame, texto)
            else:
                # Crear técnico
                try:
                    command = """
                        INSERT INTO tecnicos (nombre, cargo_id, fecha_ingreso, fecha_salida)
                        VALUES (?,?,?,?)
                    """
                    cursor.execute(
                        command, (nombre, cargo, fecha_ingreso, fecha_salida)
                    )
                    connection.commit()
                    cargar_tecnicos(tabla_tecnicos)
                    # Limpiar campos de frmulario
                    nombre_c.delete(0, tk.END)
                    fecha_i_c.delete(0, tk.END)
                    fecha_s_c.delete(0, tk.END)
                    cargo_c.delete(0, tk.END)
                except Exception as e:
                    # Mostrar error en la creación
                    logger.error("No se pudo crear el tecnico: %s", e)
                    ErrorAlert(frame, "Error al crear el técnico")
        # Ventanas de alerta de validaciones
        else:
            AdverteciaAlerta(frame, "Complete todos los campos")
    else:
        AdverteciaAlerta(frame, "Fecha inválida \nFormato correcto: YYYY-MM-DD")
