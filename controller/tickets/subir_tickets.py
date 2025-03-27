from model.connection import *
from controller.data.obtener_data import *
from controller.data.validaciones import *
from controller.data.cargar_datos import *
from controller.data.mostrar import *
from controller.tickets.consultar import *
from view.alertas.correcto import *
from view.alertas.error import *
from logs.logger_config import logger


# Cargar tickets abiertos en la tabla especificada
def subir_tickets(tabla, frame, reporte, progress):
    connection = connection_to_db()
    cursor = connection.cursor()
    """
    Carga datos desde un archivo y los inserta o actualiza en la base de datos de tickets.

    Parámetros:
    tabla -- Widget de interfaz donde se mostrarán los datos actualizados.
    """
    try:
        if reporte is None:
            # Regresa error si el CSV esta vacio
            ErrorAlert(frame, "Tipo de archivo vacio o \nTipo de archivo incorrecto")
            return

        # Obtner tickets de la base de datos
        command_R = "SELECT id_ticket FROM tickets;"
        cursor.execute(command_R)
        tickets = cursor.fetchall()

        # Obtener tecnicos de la base de datos
        command_T = "SELECT id_tecnico, nombre, cargo_id FROM tecnicos"
        cursor.execute(command_T)
        tecnicos = list(cursor.fetchall())

        # COntadores para seguimiento de registros
        actualizados = 0  # Registros actualizados
        nuevos = 0  # Registros insertados

        # Recorrer csv para procesafr de datos
        for indice, row in reporte.iterrows():
            existe = False  # Verificar si existe
            id_ticket = int(indice)  # Se define el código del ticket

            # Extraer datos del registro iterado
            titulo = row.values[0]
            estado = row.values[3]
            fecha_apertura = row.values[4]
            fecha_limite = row.values[5]
            categoria = row.values[6]
            prioridad = row.values[7]
            solicitante = row.values[8]
            tecnico_i = str(row.values[9])  # técnico aasignado
            localizacion = row.values[12]
            revisado = "No revisado"
            observacion = " "  # Observaciones vacías por defecto

            # Validar si el ticket existe en base de datos
            for ticket in tickets:
                if ticket[0] == id_ticket:
                    existe = True
                    break

            if existe:
                actualizados = +1
                # Obtener el técnico actual y estado del ticket en la base de datos
                command_F = "SELECT tecnico_id, estado FROM tickets WHERE id_ticket = ?"
                cursor.execute(command_F, (id_ticket,))
                result = cursor.fetchone()
                tecnico_actual, estado_actual = result[0], result[1]

                # Normalizar los nombres de los técnicos para comparar
                tecnico_normalizado = normalizar_nombre(tecnico_i)
                tecnico_actual_nombre = next(
                    (
                        normalizar_nombre(t[1])
                        for t in tecnicos
                        if str(t[0]) == str(tecnico_actual)
                    ),
                    "",
                )

                cambios = False  # Indica si hubo cambios

                # Si el técnico cambió y no es None ni 'Sin asignar', se actualiza
                if (
                    tecnico_i != None
                    or tecnico_normalizado != tecnico_actual_nombre
                    or tecnico_i != "Sin asignar"
                ):
                    for t in tecnicos:
                        if tecnico_i == t[1]:  # Buscar técnico en base de datos
                            tecnico_i = obtener_id_tecnico(tecnico_i)
                            cambios = True

                # Si el estado cambió, se marca como cambio
                if estado != estado_actual:
                    cambios = True

                # Si hubo cambios, actualiza ticket en base de datos
                if cambios:
                    try:
                        command = """
                            UPDATE tickets
                            SET tecnico_id = ?, estado = ?
                            WHERE id_ticket = ?
                        """
                        cursor.execute(command, (tecnico_i, estado, id_ticket))
                        connection.commit()
                        break
                    except Exception as e:
                        print(e, "c")
            else:
                nuevos += 1
                # Se asigna técnico default si no hay tecnico en la fila
                if tecnico_i == None:
                    tecnico_i = "1"
                else:
                    # Buscar técnico en vase de datos
                    for t in tecnicos:
                        if str(t[1]) == str(tecnico_i):
                            tecnico_i = obtener_id_tecnico(tecnico_i)
                            break
                    else:
                        # Si no se encuentra se coloca valor por defecto
                        tecnico_i = "1"

                # Intentar insertar un nuevo ticket en base de datos
                try:
                    command = """
                    INSERT INTO tickets(id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
                    prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, script_id, observaciones, revisado)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?) 
                    """
                    cursor.execute(
                        command,
                        (
                            id_ticket,
                            titulo,
                            estado,
                            fecha_apertura,
                            fecha_limite,
                            categoria,
                            prioridad,
                            solicitante,
                            localizacion,
                            tecnico_i,
                            "5",
                            "54",
                            observacion,
                            revisado,
                        ),
                    )
                    connection.commit()

                    nuevos += 1  # Incrementa contador de tickets insertados
                except Exception as e:
                    logger.error("No se lograron cargar los tickets %s", e)
                    ErrorAlert(frame, "Error al cargar los datos")

        # Actualizar interfaz con los datos de la base de datos
        mostrar_datos(query_datos(), tabla)
    except Exception as e:
        logger.error("No se lograron cargar los datos: %s", e)
        ErrorAlert(frame, "Error al subir los datos")
    finally:
        progress.destroy()
        # Mostrar mensaje de exito con la cantidad de registros procesados
        if actualizados > 0 and nuevos > 0:
            Completado(
                frame,
                f"Se cargaron correctamente {nuevos} registros nuevos \nSe actualizaron {actualizados} tickets",
            )
        elif nuevos > 0 and actualizados == 0:
            Completado(frame, f"Se subieron {nuevos} tickets nuevos")
        elif actualizados == 0 and nuevos == 0:
            Completado(frame, f"No se cargó ningún registro nuevo")
        else:
            ErrorAlert(frame, "Archivo vacio/icorrecto")
