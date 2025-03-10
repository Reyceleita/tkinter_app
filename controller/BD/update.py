
from logs.logger_config import logger
from model.connection import *
from view.alertas.error import *
from view.alertas.correcto import *

conn = connection_to_db()
cursor = conn.cursor()

msg_ok = 'Registro modificado correctamente'
msg_fail = 'Error al guaradar los cambios'

def update_valor(frame, id, nombre, tabla, campo, valor):
    conn = connection_to_db()
    cursor = conn.cursor()
    try:
        update =  f"""
            UPDATE {tabla} 
            SET {campo} = ?
            WHERE {valor} = ?
        """
        
        cursor.execute(update, (nombre, id))
        conn.commit()
        Completado(frame, msg_ok)
    except Exception as e:
        logger.error(f'No se pudo actualizar: {e}')
        ErrorAlert(frame, msg_fail)
    finally:
        if conn:
            conn.close()