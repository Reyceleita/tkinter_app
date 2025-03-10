
from logs.logger_config import logger
from model.connection import *
from view.alertas.error import *
from view.alertas.correcto import *


msg_ok = 'Se eliminó correctamente'
msg_fail = 'Error en la eliminación'

def delete(frame, id, tabla, campo):
    conn = connection_to_db()
    cursor = conn.cursor()
    try:
        delete = f"""
            DELETE FROM {tabla}
            WHERE {campo} = ?
        """
        
        cursor.execute(delete, (id, ))
        conn.commit()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo eliminar: {e}')
        ErrorAlert(frame, msg_fail)
    finally:
        conn.close()
