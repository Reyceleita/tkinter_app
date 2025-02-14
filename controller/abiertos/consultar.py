from model.connection import *
from controller.data.mostrar import *

connection = connection_to_db()
cursor = connection.cursor()

#Listar datos de tickets abiertos
def query_datos_activos():    
    datos=list()
    
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

#Filtrar según campos con los tickets abiertos
def filtar_id_abiertos(id_filtro, columna_filtro, tabla, conteo):
    id_filtro = id_filtro.lower()
    datos = query_datos_activos()
    a = []
    columnas = {
        'Código': 0,
        'Título': 1,
        'Fecha de apertura': 2,
        'Fecha límite': 3,
        'Categoría': 4,
        'Técnico asignado': 5,
        'Solución': 6,
        'Script': 7,
        'Fecha de Soclución': 8,
        'Observaciones': 9,
        'Estado': 10,
        'Revisado': 11,
    }
    def columna(columna):
        return columnas.get(columna, 'NA')
    
    campo = columna(str(columna_filtro))
    
    
    if id_filtro.strip() != "" :
        for row in datos:
            id_a = str(row[campo])
            if id_filtro in id_a.lower():
                a.append(row)
        mostrar_datos(a, tabla)
        conteo.set(mostrar_datos(a, tabla))
    else:
        conteo.set(mostrar_datos(datos, tabla))
        mostrar_datos(datos, tabla)