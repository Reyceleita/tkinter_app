import sqlite3
import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "tkinter_app"
}

#Conexión a la base de datos
# def connection_to_db():
#     connection = sqlite3.connect('./model/database/db.sqlite')
#     return connection

def connection_to_db():
    connection = mysql.connector.connect(**config)
    return connection
