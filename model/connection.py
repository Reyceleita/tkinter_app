import sqlite3
from logs.logger_config import logger

#Conexión a la base de datos
def connection_to_db():
    try:
        connection = sqlite3.connect('./model/database/db.sqlite')
        return connection
    except sqlite3.Error as e:
        print('Error en la conexión')
        logger.error('Conexion a base de datos fallida: %s', e)