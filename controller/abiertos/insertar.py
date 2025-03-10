from model.connection import *
import datetime


#Subir a base de datos nuevos tickets abiertos
def insertar_abierto(id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
        prioridad, solicitante, localizacion, tecnico_i, observacion, estado_t, revisado):
    connection = connection_to_db()
    cursor =  connection.cursor()
    command = """
    INSERT INTO tickets_diarios(
        id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
        prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, 
        script_id, observaciones, fecha_actualiza, estado_t, revisado
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %X")
    cursor.execute(command, (
        id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
        prioridad, solicitante, localizacion, tecnico_i, '5', '54', 
        observacion, fecha_actual, estado_t, revisado
    ))
    connection.commit()
    