from tkinter import messagebox

from model.connection import *
from controller.abiertos.consultar import *
from controller.data.mostrar import *
from controller.tickets.consultar import *
from view.alertas.correcto import *
from view.alertas.error import *
from logs.logger_config import logger


#Pasar tickets resueltos a la respectiva tabla.
def cerrar_abierto(tabla, frame):
    connection = connection_to_db()
    cursor =  connection.cursor()
    try:
        #Traer datos necesarios
        revisados = query_revisados_abiertos() #Tickets abiertos en estado revisado
        cerrados = query_tickets() #Tickets ya cerrados
        conteo = 0 #Contador de tickets modificados
        for row in revisados:
            conteo += 1 #Aumento del conteo
            existe = False #Reinicio de estado

            #Asignación de datos para la inserción
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

            #Verificar existencia del ticket abierto en tickets
            for ticket in cerrados:
                if ticket[0] == id_ticket:
                    existe = True
                    break
                
            if existe:
                #Actualizar solo lo necesario si el ticket abierto existía
                command = """
                    UPDATE tickets
                    SET forma_solucion_id = ?, tecnico_id = ?, script_id = ?, fecha_solucion = ?, observaciones =  ?, revisado = 'Revisado'
                    WHERE id_ticket = ?
                """
                cursor.execute(command, (forma_solucion_id, tecnico_id, script_id, fecha_solucion, observaciones, id_ticket))
                connection.commit()
            else:
                #Agregar el ticket abierto por completo a la tabla
                command = """
                    INSERT INTO tickets(
                        id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
                        prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, 
                        script_id, fecha_solucion, observaciones, revisado
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(command, (id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, script_id, fecha_solucion, observaciones, revisado))
                connection.commit()

            #Eliminar el ticket de la tabla abiertos
            cursor.execute("DELETE FROM tickets_diarios WHERE id_ticket = ?", (id_ticket, ))
            connection.commit()
        mostrar_datos(query_datos_activos(), tabla)

    #Mostrar ventanas de información:
        if conteo == 0:
            Completado(frame, 'No se cerró nigún ticket')
        else:
            Completado(frame, f'Se cerraron correctamente {conteo} tickets')
    except Exception as e:
        logger.error('No se lograron cerrar los tickets: %s', e)
        ErrorAlert(frame, 'Error al cerrar revisados')