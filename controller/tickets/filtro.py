from model.connection import *


# Filtrar según valores ingresados
def filtro(tabla, filter=None):

    # Conectar a base de datos local
    connection = connection_to_db()
    cursor = connection.cursor()

    # Eliminar datos mostrados en tabla
    tabla.delete(*tabla.get_children())

    # Query para consultar datos
    query = """
        SELECT id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, localizacion, nombre, solucion, script, fecha_solucion, observaciones, revisado 
        FROM tickets
        INNER JOIN tecnicos ON tickets.tecnico_id = tecnicos.id_tecnico 
        INNER JOIN forma_solucion ON tickets.forma_solucion_id = forma_solucion.id_solucion
        INNER JOIN scripts ON tickets.script_id = scripts.id_script
        WHERE 1=1
    """

    # Columnas para filtrar
    columnas = {
        "Código": "id_ticket",
        "Título": "titulo",
        "Estado": "estado",
        "Fecha de apertura": "fecha_apertura",
        "Fecha límite": "fecha_limite",
        "Categoría": "categoria",
        "Localización": "localizacion",
        "Técnico encargado": "nombre",
        "Solucion": "solucion",
        "Script": "script",
        "Fecha de solución": "fecha_solucion",
        "Observaciones": "observaciones",
        "Revisado": "revisado",
    }

    valor = []

    if filter:
        for col, value in filter.items():
            db_col = columnas.get(col)
            # Agregar valores para filtrar
            if str(value.strip()) != "":
                query += f" AND {db_col} LIKE ?"  # Agregar tabla a filtrar
                valor.append(f"%{value}%")  # Aagregar dato por el cuál filtrar
        query += "ORDER BY fecha_apertura DESC"  # Aagregar tabla y valor a la query

    # Ejecutar query
    cursor.execute(query, valor)
    resultado = cursor.fetchall()  # Guardar resultado

    # Cargar datos en la tabla
    for linea in resultado:
        tabla.insert("", "end", value=linea)

    return resultado
