from model.connection import *
from controller.data.mostrar import *

connection = connection_to_db()
cursor = connection.cursor()


# Listar datos de tickets abiertos
def query_datos_activos():
    datos = list()

    command = """
        SELECT id_ticket, titulo, fecha_apertura, fecha_limite, categoria, nombre, solucion, script, fecha_solucion, observaciones, estado_t, revisado
        FROM tickets_diarios
        INNER JOIN tecnicos ON tickets_diarios.tecnico_id = tecnicos.id_tecnico
        INNER JOIN forma_solucion ON tickets_diarios.forma_solucion_id = forma_solucion.id_solucion
        INNER JOIN scripts ON tickets_diarios.script_id = scripts.id_script;
    """
    cursor.execute(command)
    datos.clear()
    datos = list(cursor.fetchall())

    return datos


# Listar datos de tivkets revisados
def query_revisados_abiertos():
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
