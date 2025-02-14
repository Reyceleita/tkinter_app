from tkinter import messagebox
from model.connection import *
from controller.data.validaciones import *
from controller.data.obtener_data import *
from controller.data.mostrar import *
from controller.abiertos.consultar import *

connection = connection_to_db()
cursor =  connection.cursor()

#Fucnión para actualizar el estado de un ticket abierto
def actualizar_estado_abiertos(estado, ticket):
    cursor.execute('UPDATE tickets_abiertos SET estado_t = %s WHERE id_ticket = %s', (estado, ticket))
    connection.commit()

#Actualizar estado del ticket abiento en base de datos
def actualizar_abiertos(tecnico_i, estado, fecha_actu, estado_t, id_ticket):
    command = """
        UPDATE tickets_diarios
        SET tecnico_id = %s, estado = %s, fecha_actualiza = %s, estado_t = %s
        WHERE id_ticket = %s
    """
    cursor.execute(command, (tecnico_i, estado, fecha_actu, estado_t, id_ticket))
    connection.commit()

#Actualizar datos del ticket abierto en base de datos
def actualizar_abierto(id_ticket, solucion, tecnico, script, fecha, observacion, frame, tecnico_list, script_list, solucion_list, tabla):
    solucion_id = obtener_campo_lista(solucion_list, solucion)
    tecnico_id = obtener_campo_lista(tecnico_list, tecnico)
    script_id = obtener_campo_lista(script_list, script)
    observacion = str(observacion)
    command = """
        UPDATE tickets_diarios
        SET forma_solucion_id = %s, tecnico_id = %s, script_id = %s, fecha_solucion = %s, observaciones =  %s, revisado = 'Revisado'
        WHERE id_ticket = %s
    """
    
    if validar_fecha(fecha.strip()):
        if solucion_id is not None and tecnico_id is not None and solucion_id is not None:
            if observacion.strip() == "":
                observacion = 'Sin observaciones'
            
            try:
                cursor.execute(command, (solucion_id, tecnico_id, script_id, fecha, observacion, id_ticket))
                connection.commit()
                frame.destroy()
            except Exception as e:
                print(e)
            
            mostrar_datos(query_datos_activos(), tabla)
        else:
            messagebox.showerror('Error', 'Complete todos los campos')
            frame.lift()
    else:
        messagebox.showerror('Error', 'Fecha inválida \nFormato correcto: YYYY-MM-DD')
        frame.lift()
    
#Función para obtener campos especificos de un ticket específico
def obtener_desplegables(id):
    command = """
        SELECT nombre, solucion, script, fecha_solucion
        FROM tickets_diarios
        INNER JOIN tecnicos ON tickets_diarios.tecnico_id = tecnicos.id_tecnico
        INNER JOIN forma_solucion ON tickets_diarios.forma_solucion_id = forma_solucion.id_solucion
        INNER JOIN scripts ON tickets_diarios.script_id = scripts.id_script
        WHERE id_ticket = %s
    """
    cursor.execute(command, (id, ))
    info = list(cursor.fetchall()[0])
    return info