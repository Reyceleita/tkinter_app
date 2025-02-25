import sqlite3
import pandas as pd
import os

# Ruta donde se guardarán los CSV
output_folder = r"..\csv"

# Conectar con SQLite
conn = sqlite3.connect(r"C:\Users\ivanfceleitar\Documents\GitHub\tkinter_app\model\database\db.sqlite")

# Obtener nombres de todas las tablas
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)

# Exportar cada tabla a un archivo CSV
for table in tables["name"]:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    
    # Guardar como CSV
    csv_path = os.path.join(output_folder, f"{table}.csv")
    df.to_csv(csv_path, index=False)

conn.close()

print(f"Se han guardado {len(tables)} tablas como archivos CSV en {output_folder}")
