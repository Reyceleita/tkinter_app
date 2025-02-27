from tkinter import messagebox

from model.connection import *
from controller.abiertos.consultar import *
from controller.data.mostrar import *
from controller.tickets.consultar import *
from view.alertas.correcto import *

connection = connection_to_db()
cursor = connection.cursor()

def cerrar_abierto(tabla, frame):
    revisados = query_revisados_abiertos()
    cerrados = query_tickets()
    
    for row in revisados:
        existe = False
        
        id_ticket = row[0]
        titulo = row[1]
        estado = row[2]
        fecha_apertura = row[3]
        fecha_limite = row[4]
        categoria = row[5]
        prioridad = row[6]
        solicitante = row[7]
        localizacion = row[8]
        tecnico_id = row[9]
        forma_solucion_id = row[10]
        script_id = row[11]
        fecha_solucion = row[12]
        observaciones = row[13]
        revisado = row[14]
        
        for ticket in cerrados:
            if ticket[0] == id_ticket:
                existe = True
                break
        
        if existe:
            command = """
                UPDATE tickets
                SET forma_solucion_id = ?, tecnico_id = ?, script_id = ?, fecha_solucion = ?, observaciones =  ?, revisado = 'Revisado'
                WHERE id_ticket = ?
            """
            cursor.execute(command, (forma_solucion_id, tecnico_id, script_id, fecha_solucion, observaciones, id_ticket))
            connection.commit()
        else:
            command = """
                INSERT INTO tickets(
                    id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
                    prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, 
                    script_id, fecha_solucion, observaciones, revisado
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(command, (id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, script_id, fecha_solucion, observaciones, revisado))
            connection.commit()
        
        cursor.execute("DELETE FROM tickets_diarios WHERE id_ticket = ?", (id_ticket, ))
        connection.commit()
        
    mostrar_datos(query_datos_activos(), tabla)
    Completado(frame, 'Se cerraron correctamente')