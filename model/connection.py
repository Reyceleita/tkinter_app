import sqlite3

#Conexión a la base de datos
def connection_to_db():
    connection = sqlite3.connect('./model/database/db.sqlite')
    return connection
