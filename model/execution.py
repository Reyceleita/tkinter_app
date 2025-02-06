from .connection import *
import os

connection = connection_to_db()
cursor = connection.cursor()

#script para crear base de datos una vez
def first_execute():
    cursor.execute("CREATE TABLE IF NOT EXISTS execution_log (executed INTEGER)")
    cursor.execute("SELECT executed FROM execution_log")
    result = cursor.fetchone()

    if not result:
        from model import script
        cursor.execute("INSERT INTO execution_log (executed) VALUES (1)")
        connection.commit()