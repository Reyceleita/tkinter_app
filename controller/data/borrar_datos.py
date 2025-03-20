from view.alertas.correcto import *
from model.connection import *
from logs.logger_config import logger
from view.alertas.error import *


# Vaciar base de datos local
def eliminar_db(frame):

    conn = connection_to_db()
    cursor = conn.cursor()
    # Tablas a limpiar
    tablas = ("tickets", "tickets_diarios")

    try:
        for tabla in tablas:
            cursor.execute(f"DELETE FROM {tabla}")  # Se limpia la tabla

        conn.commit()
        conn.close()

        with connection_to_db() as conn_vacuum:
            conn_vacuum.execute("VACUUM")
        frame.destroy()
    except Exception as e:
        logger.error("No se eliminó la base de datos: %s", e)
        ErrorAlert(frame, "Error al vaciar la base de datos")
