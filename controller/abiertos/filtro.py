from model.connection import *

connection = connection_to_db()
cursor = connection.cursor()

def nose(tabla, filter=None ):
    
    tabla.delete(*tabla.get_children())
    
    q = """
        SELECT Código, Título, Fecha de apertura, Fecha límite, 
        Categoría, Técnico encargado, Solucion, 
        Script Fecha de solución, Observaciones, Estado, Revisado 
        FROM tickets_diarios
        WHERE 1=1
    """
    p = []
    
    if filter:
        for col, value in filter.items():
            if value:
                q +=f"AND {col} LIKE ?"
                p.append(f"%{value}")
    
    cursor.execute(q,(p, ))
    r = cursor.fetchall()
    
    for ri in r:
        tabla.insert("", "end", values=ri) 

