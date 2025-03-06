
from logs.logger_config import logger
from model.connection import *
from view.alertas.error import *
from view.alertas.correcto import *

conn = connection_to_db()
cursor = conn.cursor()

msg_ok = 'Registro creado correctamente'
msg_fail = 'Error en la creación'

def insert_cargo(frame, valor):
    try:
        insert = """
            INSERT INTO cargos (cargo)
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

def insert_solucion(frame, valor):
    try:
        insert = """
            INSERT INTO forma_solucion (solucion)
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

def insert_script(frame, valor):
    try:
        insert = """
            INSERT INTO scripts (script)
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