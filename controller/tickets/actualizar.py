from tkinter import messagebox

from model.connection import *
from controller.data.obtener_data import *
from controller.data.validaciones import *
from controller.tickets.consultar import *

connection = connection_to_db()
cursor = connection.cursor()

def actualizar_ticket(id_ticket, solucion, tecnico, script, fecha, observacion, frame, tecnico_list, script_list, solucion_list, tabla):
    solucion_id = obtener_campo_lista(solucion_list, solucion)
    tecnico_id = obtener_campo_lista(tecnico_list, tecnico)
    script_id = obtener_campo_lista(script_list, script)
    observacion = str(observacion)
    
    command = """
    UPDATE tickets
    SET forma_solucion_id = %s, tecnico_id = %s, script_id = %s, fecha_solucion = %s, observaciones =  %s, revisado = 'Revisado'
    WHERE id_ticket = %s
    """
    
    if validar_fecha(fecha.strip()):
        if solucion_id is not None and tecnico_id is not None and solucion_id is not None:
            if observacion.strip() == "":
                observacion = "Sin observaciones"
            
            cursor.execute(command, (solucion_id, tecnico_id, script_id, fecha, observacion, id_ticket))
            connection.commit()
            frame.destroy()
            mostrar_datos(query_datos(), tabla)
        else: 
            messagebox.showerror('Error', 'Complete todos los campos')
            frame.lift()
            
    else:
        messagebox.showerror('Error', 'Fecha inválida \nFormato correcto: YYYY-MM-DD')
        frame.lift()