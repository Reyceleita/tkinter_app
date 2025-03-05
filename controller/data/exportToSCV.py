import sqlite3
import pandas as pd
import os
from model.connection import *

from view.alertas.error import *
from view.alertas.correcto import *
from logs.logger_config import logger

# Carpeta donde se guardarán los CSV
output_folder = r"..\csv"

# Crear la carpeta si no existe
os.makedirs(output_folder, exist_ok=True)

# Conectar con SQLite
conn = connection_to_db()

def exportar_datos(frame):
    try:
        # Obtener nombres de todas las tablas
        tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)

        # Exportar cada tabla a un archivo CSV
        for table in tables["name"]:
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)

            # Guardar como CSV
            csv_path = os.path.join(output_folder, f"{table}.csv")
            df.to_csv(csv_path, index=False)

        conn.close()

        Completado(frame, f"Se han guardado {len(tables)} tablas como archivos CSV en {output_folder}")
    except Exception as e:
        logger.error('No se pudo exportar %s', e)
        ErrorAlert(frame, 'Error al exportar')
