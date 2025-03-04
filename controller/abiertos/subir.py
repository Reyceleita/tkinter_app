import datetime

from model.connection import *
from controller.data.obtener_data import *
from controller.abiertos.actualizar import *
from controller.abiertos.consultar import *
from controller.abiertos.insertar import *
from controller.data.cargar_datos import *
from controller.data.mostrar import *
from view.alertas.correcto import *
from view.alertas.progressbar import *

connection = connection_to_db()
cursor = connection.cursor()

def subir_abiertos(tabla, frame, reporte, progressbar):
    try: 
        conteo_actu = 0
        conteo_esc = 0
        coneto_nuevo = 0
        conteo_sin = 0
        tickets_csv = list()

        if reporte is None:
            ex = 'Documento vacio'
            return ex

        for indice, row in reporte.iterrows():
            tickets_csv = {int(indice) for indice in reporte.index} 

        command = "SELECT id_ticket FROM tickets_diarios;"
        cursor.execute(command)
        tickets_db = cursor.fetchall()
        command = "SELECT id_tecnico, nombre FROM tecnicos"
        cursor.execute(command)
        tecnicos_db = list(cursor.fetchall())

        for indice, row in reporte.iterrows():
            existe = False
            id_ticket_csv = int(indice)
            titulo_csv = row.values[0]
            ultima_actu_csv = str(row.values[2])
            estado_csv = row.values[3]
            fecha_apertura_csv = row.values[4]
            fecha_limite_csv = row.values[5]
            categoria_csv = row.values[6]
            prioridad_csv = row.values[7]
            solicitante_csv = row.values[8]
            tecnico_csv = str(row.values[9])
            localizacion_csv = row.values[12]
            revisado = "No revisado"
            observacion = " "

            for ticket in tickets_db:
                if ticket[0] == id_ticket_csv:
                    existe = True
                    break
                
            if existe:
                cambio = False
                ticket_info = obtener_ticket_abierto(id_ticket_csv)

                tecnico_db, estado_db, fecha_db, revisado_db = ticket_info[0], ticket_info[1], ticket_info[2], ticket_info[3]

                nombre_normalizado = normalizar_nombre(tecnico_csv)
                nombre_db = next(
                    (normalizar_nombre(t[1]) for t in tecnicos_db if str(t[0]) == str(tecnico_db))
                )

                if tecnico_csv != None and nombre_normalizado != nombre_db and tecnico_csv != 'sin asignar':
                    tecnico_csv = obtener_id_tecnico(tecnico_csv)
                    cambio = True

                if estado_csv != estado_db:
                    cambio = True

                if revisado_db == 'Revisado':
                    cambio = False

                ultima_actu_csv = datetime.datetime.strptime(ultima_actu_csv, '%Y-%m-%d %H:%M')
                fecha_db = datetime.datetime.strptime(fecha_db, '%Y-%m-%d %H:%M:%S')
                if fecha_db < ultima_actu_csv:
                    estado_t = 'Actualizado'
                elif ultima_actu_csv < fecha_db:
                    estado_t = 'Sin cambios'

                if cambio:
                    fecha_db = datetime.datetime.now().strftime("%Y-%m-%d %X")
                    actualizar_abiertos(tecnico_csv,estado_csv,fecha_db, estado_t,id_ticket_csv)
                    conteo_actu +=1
                else:
                    estado_t = 'Sin cambios'
                    actualizar_estado_abiertos(estado_t, id_ticket_csv)
            else:
                estado_t = 'Nuevo'
                coneto_nuevo +=1
                if tecnico_csv == None:
                    tecnico_csv = '1'
                else:
                    tecnico_csv = obtener_id_tecnico(tecnico_csv)

                try:
                    insertar_abierto(id_ticket_csv,titulo_csv, estado_csv, fecha_apertura_csv,
                                    fecha_limite_csv, categoria_csv, prioridad_csv, solicitante_csv,
                                    localizacion_csv, tecnico_csv, observacion, estado_t, revisado)
                except Exception as e:
                    print('error', e)

        for ticket in tickets_db:
            ticket = ticket[0]
            estado = obtener_estado(ticket)
            if ticket not in tickets_csv: 
                if estado == 'Nuevo' or estado == 'Sin cambios':
                    actualizar_estado_abiertos('Escalado', ticket)
                    conteo_esc +=1
                else:
                    conteo_sin +=1

        mostrar_datos(query_datos_activos(), tabla)
    except sqlite3.Error as e:
        ErrorAlert(frame, e)
    
    finally:
        progressbar.destroy()
        Completado(frame, f'Se cargaron correctamente los registros \nSe agregaron {coneto_nuevo} tickers \nSe actualizaron {conteo_actu} tickets \nSe escalaron {conteo_esc} tickets \n{conteo_sin} tickets no tuvieron cambios')