from model.connection import *
from controller.data.mostrar import *


# Listar datos de tickets abiertos
def query_datos_activos():
    connection = connection_to_db()
    cursor = connection.cursor()
    datos = list()

    command = """
        SELECT id_ticket, titulo, fecha_apertura, fecha_limite, categoria, nombre, solucion, script, fecha_solucion, observaciones, estado_t, revisado
        FROM tickets_diarios
        LEFT JOIN tecnicos ON tickets_diarios.tecnico_id = tecnicos.id_tecnico
        LEFT JOIN forma_solucion ON tickets_diarios.forma_solucion_id = forma_solucion.id_solucion
        LEFT JOIN scripts ON tickets_diarios.script_id = scripts.id_script
        ORDER BY fecha_apertura DESC;
    """
    cursor.execute(command)
    datos.clear()
    datos = list(cursor.fetchall())

    return datos


# Listar datos de tivkets revisados
def query_revisados_abiertos():
    connection = connection_to_db()
    cursor = connection.cursor()
    datos = list()

    command = """
        SELECT id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, prioridad, solicitante,
        localizacion, tecnico_id, forma_solucion_id, script_id, fecha_solucion, observaciones, revisado
        FROM tickets_diarios
        WHERE revisado = 'Revisado'
    """

    cursor.execute(command)
    datos.clear()
    datos = list(cursor.fetchall())
    return datos
