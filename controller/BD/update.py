
from logs.logger_config import logger
from model.connection import *
from view.alertas.error import *
from view.alertas.correcto import *

conn = connection_to_db()
cursor = conn.cursor()

msg_ok = 'Registro modificado correctamente'
msg_fail = 'Error al guaradar los cambios'

def update_cargos(frame, id, nombre):
    try:
        update = """
            UPDATE cargos
            SET cargo = ?
            WHERE id_cargo = ?
        """

        cursor.execute(update, (nombre, id))
        conn.commit()
        conn.close()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo actualizar: {e}')
        ErrorAlert(frame, msg_fail)
        conn.close()

def update_solucion(frame, id, nombre):
    try:
        update = """
            UPDATE forma_solucion
            SET solucion = ?
            WHERE id_solucionn = ?
        """
        
        cursor.execute(update, (nombre, id))
        conn.commit()
        conn.close()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo actualizar: {e}')
        ErrorAlert(frame, msg_fail)
        conn.close()

def update_script(frame, id, nombre):
    try:
        update =  """
            UPDATE scripts 
            SET script = ?
            WHERE id_script = ?
        """
        
        cursor.execute(update, (nombre, id))
        conn.commit()
        conn.close()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo actualizar: {e}')
        ErrorAlert(frame, msg_fail)
        conn.close()
