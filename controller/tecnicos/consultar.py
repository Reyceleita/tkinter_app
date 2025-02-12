import datetime

from model.connection import *

connection = connection_to_db()
cursor = connection.cursor()


def cargar_tecnicos(tabla_tecnicos):
    """
    cargar los datos, de la base de datos
    
    """
    for row in tabla_tecnicos.get_children():
        tabla_tecnicos.delete(row)
    
    command = """
        SELECT id_tecnico, nombre, cargo, fecha_ingreso, fecha_salida 
        FROM tecnicos
        INNER JOIN cargos ON cargos.id_cargo = tecnicos.cargo_id
        WHERE id_tecnico > 1
    """

    cursor.execute(command)
    tecnicos = cursor.fetchall()
    fecha_hoy = datetime.datetime.now()
    for fila in tecnicos:
        id_tecnico = str(fila[0])
        command_1 ="""
            SELECT id_ticket 
            FROM tickets 
            WHERE tecnico_id = %s
        """
        
        command_2 ="""
            SELECT id_ticket 
            FROM tickets_diarios
            WHERE tecnico_id = %s
        """
        cursor.execute(command_1, (id_tecnico, ))
        tickets = cursor.fetchall()
        conteo = 0
        conteo_d = 0
        conteo = len(tickets)
        cursor.execute(command_2, (id_tecnico, ))
        tickets_d = cursor.fetchall()
        conteo_d = len(tickets_d)
        fila = list(fila)
        fila.pop(0)
        fila.append(int(conteo_d))
        fila.append(int(conteo))
        fecha_fin = None
        
        try:
            fecha_fin = datetime.strptime(fila[3], '%Y-%m-%d')
            if fecha_fin < fecha_hoy:
                fila.append('Inactivo')
                tabla_tecnicos.insert('', 'end', values=fila)
            elif fecha_fin > fecha_hoy: 
                fila.append('Activo')
                tabla_tecnicos.insert('', 'end', values=fila)
        except:
            fila.append('N/A')
            tabla_tecnicos.insert('', 'end', values=fila)

def tecnico_nobre(nombre):
    
    command = """
            SELECT id_tecnico, cargo, fecha_ingreso, fecha_salida
            FROM tecnicos 
            INNER JOIN cargos ON cargos.id_cargo = tecnicos.cargo_id
            WHERE nombre = %s
            """
    cursor.execute(command, (nombre, ))
    tecnico = list(cursor.fetchall()[0])
    return tecnico