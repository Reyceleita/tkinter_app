from .connection import *
from model.script import *
import os


# script para crear base de datos una vez
def first_execute():
    with connection_to_db() as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS execution_log (executed INTEGER)")
        cursor.execute("SELECT executed FROM execution_log")
        result = cursor.fetchone()

        if not result:
            crear_tablas_db()
            cursor.execute("INSERT INTO execution_log (executed) VALUES (1)")
            connection.commit()
