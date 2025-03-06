
from logs.logger_config import logger
from model.connection import *
from view.alertas.error import *
from view.alertas.correcto import *

conn = connection_to_db()
cursor = conn.cursor()

msg_ok = 'Se eliminó correctamente'
msg_fail = 'Error en la eliminación'

def delete_cargo(frame, id):
    try:
        delete = """
            DELETE FROM cargos
            WHERE id_cargo = ?
        """
        
        cursor.execute(delete, (id, ))
        conn.commit()
        conn.close()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo eliminar: {e}')
        ErrorAlert(frame, msg_fail)
        conn.close()

def delete_solucion(frame, id):
    try:
        delete = """
            DELETE FROM forma_solucion
            WHERE id_solucion = ?
        """
        
        cursor.execute(delete, (id, ))
        conn.commit()
        conn.close()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo eliminar: {e}')
        ErrorAlert(frame, msg_fail)
        conn.close()

def delete_script(frame, id):
    try:
        delete = """
            DELETE FROM script
            WHERE id_script = ?
        """
        
        cursor.execute(delete, (id, ))
        conn.commit()
        conn.close()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo eliminar: {e}')
        ErrorAlert(frame, msg_fail)
        conn.close()
