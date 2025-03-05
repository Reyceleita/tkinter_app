import os

from view.alertas.correcto import *
from model.connection import *
from logs.logger_config import logger
from view.alertas.error import *

#Eliminar base de datos local
def eliminar_db(frame):
    
    conn = connection_to_db()
    conn.close()
    
    try: 
        os.remove(r'.\model\database\db.sqlite')
        Completado(frame, 'Base de datos local eliminada correctamente')
    except Exception as e:
        logger.error('No se eliminó la base de datos: %s', e)
        ErrorAlert(frame, 'Error al eliminar la bases de datos')