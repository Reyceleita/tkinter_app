from model.connection import *

connection = connection_to_db()
cursor = connection.cursor()


def filtro(tabla, filter=None):

    tabla.delete(*tabla.get_children())

    q = """
        SELECT id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, localizacion, nombre, solucion, script, fecha_solucion, observaciones, revisado 
        FROM tickets
        INNER JOIN tecnicos ON tickets.tecnico_id = tecnicos.id_tecnico 
        INNER JOIN forma_solucion ON tickets.forma_solucion_id = forma_solucion.id_solucion
        INNER JOIN scripts ON tickets.script_id = scripts.id_script
        WHERE 1=1
    """

    columnas = {
        'Código': 'id_ticket',
        'Título': 'titulo',
        'Estado': 'estado',
        'Fecha de apertura': 'fecha_apertura',
        'Fecha límite': 'fecha_limite',
        'Categoría': 'categoria',
        'Localización': 'localizacion',
        'Técnico encargado': 'nombre',
        'Solucion': 'solucion',
        'Script': 'script',
        'Fecha de solución': 'fecha_solucion',
        'Observaciones': 'observaciones',
        'Revisado': 'revisado',
    }

    p = []

    if filter:
        for col, value in filter.items():
            db_col = columnas.get(col)
            if str(value.strip()) != "":
                q += f" AND {db_col} LIKE ?"
                p.append(f"%{value}%")

    cursor.execute(q, p)
    r = cursor.fetchall()

    for ri in r:
        tabla.insert("", "end", value=ri)

    return r
