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

def filtar_id(id_filtro, columna_filtro, tabla, conteo):
    """
    Filtra datos según parametros especificados
    
    Parámetros: 
        id_filtro (string): valor por el que se va a filtrar los datos
        columna_filtro (ttk.combobox): Campo de la culumna por la que filtrar
        tabla (ttk.treeview): Tabla en donde cargar los datos
        conteo (tk.IntVar): Variable para actualizar el conteo
        
    Resultados:
        Se muestran datos en la tabla según el filtro
        Se actualiza conteo de filas
    """
    
    num_filtro = id_filtro.lower()
    datos = query_datos()
    a = []
    columnas = {
        'Código': 0,
        'Título': 1,
        'Estado': 2,
        'Fecha de apertura': 3,
        'Fecha límite': 4,
        'Categoría': 5,
        'Localización': 6,
        'Técnico encargado': 7,
        'Solución': 8,
        'Script': 9,
        'Fecha de Soclución': 10,
        'Observaciones': 11,
        'Revisado': 12
    }
    def columna(columna):
        return columnas.get(columna, 'NA')
    
    campo = columna(str(columna_filtro))
    if num_filtro.strip() != "" :
        for row in datos:
            id_a = str(row[campo])
            if num_filtro in id_a.lower():
                a.append(row)
        mostrar_datos(a, tabla)
        conteo.set(mostrar_datos(a, tabla))
    else:
        conteo.set(mostrar_datos(datos, tabla))
        mostrar_datos(datos, tabla)

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
        WHERE id_ticket = %s
    """
    cursor.execute(command, (id, ))
    info = list(cursor.fetchall()[0])
    return info