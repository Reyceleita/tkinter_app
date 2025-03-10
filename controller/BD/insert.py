
from logs.logger_config import logger
from model.connection import *
from view.alertas.error import *
from view.alertas.correcto import *

conn = connection_to_db()
cursor = conn.cursor()

msg_ok = 'Registro creado correctamente'
msg_fail = 'Error en la creación'


def insert(frame, valor, tabla, campo):
    conn = connection_to_db()
    cursor = conn.cursor()
    try:
        insert = f"""
            INSERT INTO {tabla} ({campo})
            VALUES (?)
        """
        cursor.execute(insert, (valor, ))
        conn.commit()
        conn.close()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo crear: {e}')
        ErrorAlert(frame, msg_fail)
        conn.close()