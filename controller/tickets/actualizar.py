from tkinter import messagebox

from model.connection import *
from controller.data.obtener_data import *
from controller.data.validaciones import *
from controller.tickets.consultar import *
from view.alertas.error import *

#Crear conexión y cursor de Base de datos
connection = connection_to_db()
cursor = connection.cursor()

def actualizar_ticket(id_ticket, solucion, tecnico, script, fecha, observacion, frame, tecnico_list, script_list, solucion_list, tabla):
    """
    Actualizar un ticket en base de datos
    
    Parámetros:
        id_ticket (tk.IntVar): código del ticket a modificar
        solucion (ttk.StringVar): Valor del combobox de solución
        tecnico (ttk.StringVar): Valor del combobox de tecnico
        script (ttk.StringVar): Valor del combobox de script
        fecha (ttk.StringVar): Valor del Entry de fecha
        observacion (ttk.StrinVar): Valor del Entry de observación
        frame (tk.TopLevel): Ventana de edición
        tecnico_list (list): Lista de técnicos
        script_list (list): Lista de scripts
        solucion_list (list): Lista de soluciones
        tabla (ttk.TreeView): Tabla donde se muestran los datos
    
    Resultado:
        Se actualiza el ticket en base de datos según parámetros establecidos
    """
    
    #Obtener datos de los campos desplegables
    solucion_id = obtener_campo_lista(solucion_list, solucion)
    tecnico_id = obtener_campo_lista(tecnico_list, tecnico)
    script_id = obtener_campo_lista(script_list, script)
    observacion = str(observacion) #Obtener dato del ampo Entry
    
    #Sentencia SQL
    command = """
    UPDATE tickets
    SET forma_solucion_id = ?, tecnico_id = ?, script_id = ?, fecha_solucion = ?, observaciones =  ?, revisado = 'Revisado'
    WHERE id_ticket = ?
    """
    
    #Validaciones previas a actualizar el ticket
    if validar_fecha(fecha.strip()):
        if solucion_id is not None and tecnico_id is not None and solucion_id is not None:
            if observacion.strip() == "":
                observacion = "Sin observaciones"
            
            cursor.execute(command, (solucion_id, tecnico_id, script_id, fecha, observacion, id_ticket))
            connection.commit()
            frame.destroy()
            mostrar_datos(query_datos(), tabla)
        else: 
            ErrorAlert(frame, 'Complete todos los campos')
            frame.lift()
            
    else:
        ErrorAlert(frame, 'Fecha inválida \nFormato correcto: YYYY-MM-DD')
        frame.lift()