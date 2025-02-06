from tkinter import messagebox
from model.connection import *
from controller.data.validaciones import *
from controller.data.obtener_data import *

connection = connection_to_db()
cursor =  connection.cursor()

#Fucnión para actualizar el estado de un ticket abierto
def actualizar_estado_abiertos(estado, ticket):
    cursor.execute('UPDATE tickets_abiertos SET estado_t = ? WHERE id_ticket = ?', (estado, ticket))
    connection.commit()

def actualizar_abiertos(tecnico_i, estado, fecha_actu, estado_t, id_ticket):
    command = """
        UPDATE tickets_diarios
        SET tecnico_id = ?, estado = ?, fecha_actualiza = ?, estado_t = ?
        WHERE id_ticket = ?
    """
    cursor.execute(command, (tecnico_i, estado, fecha_actu, estado_t, id_ticket))
    connection.commit()

def actualizar_abierto(id_ticket, solucion, tecnico, script, fecha, observacion, frame, tecnico_list, script_list, solucion_list, tabla):
    solucion_id = obtener_campo_lista(solucion_list, solucion)
    tecnico_id = obtener_campo_lista(tecnico_list, tecnico)
    script_id = obtener_campo_lista(script_list, script)
    observacion = str(observacion)
    
    command = """
        UPDATE tickets
        SET forma_solucion_id = ?, tecnico_id = ?, script_id = ?, fecha_solucion = ?, observaciones =  ?, revisado = 'Revisado'
        WHERE id_ticket = ?
    """
    
    if validar_fecha(fecha.strip()):
        if solucion_id is not None and tecnico_id is not None and solucion_id is not None:
            if observacion.strip() == "":
                observacion = 'Sin observaciones'
            
            cursor.execute(command, (solucion_id, tecnico_id, script_id, fecha, observacion, id_ticket))
        else:
            messagebox.showerror('Error', 'Complete todos los campos')
            frame.lift()
    else:
        messagebox.showerror('Error', 'Fecha inválida \nFormato correcto: YYYY-MM-DD')
        frame.lift()