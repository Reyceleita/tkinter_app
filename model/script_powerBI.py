import sqlite3
import pandas as pd 

conn = sqlite3.connect("C:\Users\ivanfceleitar\Documents\GitHub\tkinter_app\model\database\db.sqlite")

df = pd.read_sql_query("SELECT * FROM tickets_diarios", conn)

conn.close()

df.head()