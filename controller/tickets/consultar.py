from model.connection import *
from controller.data.mostrar import *

#Crear conexión y cursor de Base de datos
connection = connection_to_db()
cursor = connection.cursor()

def query_datos():
    """
    Consulta a la tabla tickers
    
    Resultados:
        list: Información del ticket 
    """
    
    command = """
    SELECT id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, localizacion, nombre, solucion, script, fecha_solucion, observaciones, revisado 
    FROM tickets
    INNER JOIN tecnicos ON tickets.tecnico_id = tecnicos.id_tecnico 
    INNER JOIN forma_solucion ON tickets.forma_solucion_id = forma_solucion.id_solucion
    INNER JOIN scripts ON tickets.script_id = scripts.id_script;
    """
    cursor.execute(command)
    datos = list(cursor.fetchall())
    return datos

def obtener_desplegables_tickets(id):
    """
    Consultar valores de llaves foraneas de un ticket
    
    Parámetros:
        id (int): Código del ticket a consultar
    
    Resultado:
        list: campos encontrados
    """
    
    command = """
        SELECT nombre, solucion, script, fecha_solucion
        FROM tickets
        INNER JOIN tecnicos ON tickets.tecnico_id = tecnicos.id_tecnico
        INNER JOIN forma_solucion ON tickets.forma_solucion_id = forma_solucion.id_solucion
        INNER JOIN scripts ON tickets.script_id = scripts.id_script
        WHERE id_ticket = ?
    """
    cursor.execute(command, (id, ))
    info = list(cursor.fetchall()[0])
    return info