from model.connection import *


# Filtrar columnas según parámetros
def filtro(tabla, filter=None):
    connection = connection_to_db()
    cursor = connection.cursor()
    tabla.delete(*tabla.get_children())

    q = """
        SELECT id_ticket, titulo, fecha_apertura, fecha_limite, categoria, nombre, solucion, script, fecha_solucion, observaciones, estado_t, revisado 
        FROM tickets_diarios
        INNER JOIN tecnicos ON tickets_diarios.tecnico_id = tecnicos.id_tecnico 
        INNER JOIN forma_solucion ON tickets_diarios.forma_solucion_id = forma_solucion.id_solucion
        INNER JOIN scripts ON tickets_diarios.script_id = scripts.id_script
        WHERE 1=1
    """

    columnas = {
        "Código": "id_ticket",
        "Título": "titulo",
        "Fecha de apertura": "fecha_apertura",
        "Fecha límite": "fecha_limite",
        "Categoría": "categoria",
        "Técnico encargado": "nombre",
        "Solucion": "solucion",
        "Script": "script",
        "Fecha de solución": "fecha_solucion",
        "Observaciones": "observaciones",
        "Estado": "estado_t",
        "Revisado": "revisado",
    }

    p = []

    if filter:
        for col, value in filter.items():
            db_col = columnas.get(col)
            if str(value.strip()) != "":
                q += f" AND {db_col} LIKE ?"
                p.append(f"%{value}%")
        q += "ORDER BY fecha_apertura DESC"

    cursor.execute(q, p)
    r = cursor.fetchall()

    for ri in r:
        tabla.insert("", "end", values=ri)

    return r
