from model.connection import *
from controller.data.validaciones import *
from controller.data.obtener_data import *
from controller.data.mostrar import *
from controller.abiertos.consultar import *
from view.alertas.warning import *
from view.alertas.error import *
from logs.logger_config import logger


# Fucnión para actualizar el estado de un ticket abierto
def actualizar_estado_abiertos(estado, ticket):
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE tickets_diarios SET estado_t = ? WHERE id_ticket = ?", (estado, ticket)
    )
    connection.commit()


# Actualizar estado del ticket abiento en base de datos
def actualizar_abiertos(tecnico_i, estado, fecha_actu, estado_t, id_ticket):
    connection = connection_to_db()
    cursor = connection.cursor()
    command = """
        UPDATE tickets_diarios
        SET tecnico_id = ?, estado = ?, fecha_actualiza = ?, estado_t = ?
        WHERE id_ticket = ?
    """
    cursor.execute(command, (tecnico_i, estado, fecha_actu, estado_t, id_ticket))
    connection.commit()


# Actualizar datos del ticket abierto en base de datos
def actualizar_abierto(
    id_ticket,
    solucion,
    tecnico,
    script,
    fecha,
    observacion,
    frame,
    tecnico_list,
    script_list,
    solucion_list,
    tabla,
):
    connection = connection_to_db()
    cursor = connection.cursor()
    try:
        solucion_id = obtener_campo_lista(solucion_list, solucion)
        tecnico_id = obtener_campo_lista(tecnico_list, tecnico)
        script_id = obtener_campo_lista(script_list, script)
        observacion = str(observacion)
        command = """
            UPDATE tickets_diarios
            SET forma_solucion_id = ?, tecnico_id = ?, script_id = ?, fecha_solucion = ?, observaciones =  ?, revisado = 'Revisado'
            WHERE id_ticket = ?
        """

        if validar_fecha(fecha.strip()):
            if (
                solucion_id is not None
                and tecnico_id is not None
                and solucion_id is not None
            ):
                if observacion.strip() == "":
                    observacion = "Sin observaciones"

                try:
                    cursor.execute(
                        command,
                        (
                            solucion_id,
                            tecnico_id,
                            script_id,
                            fecha,
                            observacion,
                            id_ticket,
                        ),
                    )
                    connection.commit()
                    frame.destroy()
                except Exception as e:
                    print(e, "uu")

                mostrar_datos(query_datos_activos(), tabla)
            else:
                texto = "Complete todos los campos"
                AdverteciaAlerta(frame, texto)
                frame.lift()
        else:
            texto = "Fecha inválida \nFormato correcto: YYYY-MM-DD"
            AdverteciaAlerta(frame, texto)
            frame.lift()
    except Exception as e:
        logger.error("No se logró actualizar el ticket: %s", e)
        ErrorAlert(frame, "Error al actualizar el ticket")


# Función para obtener campos especificos de un ticket específico
def obtener_desplegables(id):
    connection = connection_to_db()
    cursor = connection.cursor()
    command = """
        SELECT nombre, solucion, script, fecha_solucion
        FROM tickets_diarios
        LEFT JOIN tecnicos ON tickets_diarios.tecnico_id = tecnicos.id_tecnico
        LEFT JOIN forma_solucion ON tickets_diarios.forma_solucion_id = forma_solucion.id_solucion
        LEFT JOIN scripts ON tickets_diarios.script_id = scripts.id_script
        WHERE id_ticket = ?
    """
    cursor.execute(command, (id,))
    info = list(cursor.fetchall()[0])

    return info
