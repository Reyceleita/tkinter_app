from model.connection import *
from controller.data.mostrar import *


# Consultar tickets de base de datos
def query_datos():
    connection = connection_to_db()
    cursor = connection.cursor()

    # Query de consulta
    command = """
    SELECT id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, localizacion, nombre, solucion, script, fecha_solucion, observaciones, revisado 
    FROM tickets
    LEFT JOIN tecnicos ON tickets.tecnico_id = tecnicos.id_tecnico 
    LEFT JOIN forma_solucion ON tickets.forma_solucion_id = forma_solucion.id_solucion
    LEFT JOIN scripts ON tickets.script_id = scripts.id_script;
    """
    # Ejecución de consulta
    cursor.execute(command)
    datos = list(cursor.fetchall())  # Guardar resultados

    # Regresar resultados
    return datos


# Consultar datos de llaves foraneas
def obtener_desplegables_tickets(id):
    connection = connection_to_db()
    cursor = connection.cursor()

    # Query de consulta
    command = """
        SELECT nombre, solucion, script, fecha_solucion
        FROM tickets
        LEFT JOIN tecnicos ON tickets.tecnico_id = tecnicos.id_tecnico
        LEFT JOIN forma_solucion ON tickets.forma_solucion_id = forma_solucion.id_solucion
        LEFT JOIN scripts ON tickets.script_id = scripts.id_script
        WHERE id_ticket = ?
    """
    # Ejecución de consulta
    cursor.execute(command, (id,))
    info = list(cursor.fetchall()[0])  # Guardar resultados

    # Regresar resultados
    return info


# Consultar tickets de base de datos
def query_tickets():
    connection = connection_to_db()
    cursor = connection.cursor()

    # Query de consulta
    command = """
        SELECT id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, prioridad, solicitante, 
        localizacion, tecnico_id, forma_solucion_id, script_id, fecha_solucion, observaciones, revisado
        FROM tickets
    """

    # Ejecutar consulta
    cursor.execute(command)
    datos = list(cursor.fetchall())  # Guardar resultados

    # Regresar resultados
    return datos
