import datetime

from model.connection import *


# Mostrar técnicos en la tabla
def cargar_tecnicos(tabla_tecnicos):

    # Conexión a base de datos
    connection = connection_to_db()
    cursor = connection.cursor()

    # Vaciar tabla
    for row in tabla_tecnicos.get_children():
        tabla_tecnicos.delete(row)

    # Query de consulta
    command = """
        SELECT id_tecnico, nombre, cargo, fecha_ingreso, fecha_salida 
        FROM tecnicos
        LEFT JOIN cargos ON cargos.id_cargo = tecnicos.cargo_id
        WHERE id_tecnico > 1
    """

    # Ejecución de consulta
    cursor.execute(command)
    tecnicos = cursor.fetchall()  # Guardar resultados
    fecha_hoy = datetime.datetime.now()  # Obtener fecha actual

    for fila in tecnicos:
        id_tecnico = str(fila[0])
        command_1 = """
            SELECT id_ticket 
            FROM tickets 
            WHERE tecnico_id = ?
        """

        command_2 = """
            SELECT id_ticket 
            FROM tickets_diarios
            WHERE tecnico_id = ?
        """

        cursor.execute(command_1, (id_tecnico,))
        tickets = cursor.fetchall()
        conteo = 0
        conteo_d = 0
        conteo = len(tickets)
        cursor.execute(command_2, (id_tecnico,))
        tickets_d = cursor.fetchall()
        conteo_d = len(tickets_d)
        fila = list(fila)
        fila.pop(0)
        fila.append(int(conteo_d))
        fila.append(int(conteo))
        tabla_tecnicos.insert("", "end", values=fila)


# Consultar técnico por nombre
def tecnico_nobre(nombre):
    connection = connection_to_db()
    cursor = connection.cursor()

    command = """
            SELECT id_tecnico, cargo, fecha_ingreso, fecha_salida
            FROM tecnicos 
            LEFT JOIN cargos ON cargos.id_cargo = tecnicos.cargo_id
            WHERE nombre = ?
            """
    cursor.execute(command, (nombre,))
    tecnico = list(cursor.fetchall()[0])

    return tecnico
