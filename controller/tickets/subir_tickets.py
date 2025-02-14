from tkinter import messagebox

from model.connection import *
from controller.data.obtener_data import *
from controller.data.validaciones import *
from controller.data.cargar_datos import *
from controller.data.mostrar import *
from controller.tickets.consultar import *

#Crear conexión y cursor de Base de datos
connection = connection_to_db()
cursor = connection.cursor()

#Cargar tickets abiertos en la tabla especificada
def subir_tickets(tabla):
    """
    Carga datos desde un archivo y los inserta o actualiza en la base de datos de tickets.

    Parámetros:
    tabla -- Widget de interfaz donde se mostrarán los datos actualizados.
    """
    
    #Cargar datos desde un CSV
    reporte = cargar_datos()
    
    ##Agregar alerta de error
    if reporte is None:
        #Regresa error si el CSV esta vacio
        exce = 'Documento vacio'
        return exce
    
    #Obtner tickets de la base de datos
    command_R = "SELECT id_ticket FROM tickets;"
    cursor.execute(command_R)
    tickets = cursor.fetchall()
    
    #Obtener tecnicos de la base de datos
    command_T = "SELECT id_tecnico, nombre, cargo_id FROM tecnicos"
    cursor.execute(command_T)
    tecnicos = list(cursor.fetchall())
    
    #COntadores para seguimiento de registros
    actualizados = 0 #Registros actualizados
    nuevos = 0 #Registros insertados
    
    #Recorrer csv para procesafr de datos
    for indice, row in reporte.iterrows():
        existe = False #Verificar si existe
        id_ticket = int(indice) #Se define el código del ticket
        
        #Extraer datos del registro iterado
        titulo = row.values[0]
        estado = row.values[3]
        fecha_apertura = row.values[4]
        fecha_limite = row.values[5]
        categoria = row.values[6]
        prioridad = row.values[7]
        solicitante = row.values[8]
        tecnico_i = str(row.values[9]) #técnico aasignado
        localizacion = row.values[12]
        revisado = "No revisado"
        observacion = " " #Observaciones vacías por defecto
        
        #Validar si el ticket existe en base de datos
        for ticket in tickets:
            if ticket[0] == id_ticket:
                existe = True
                break
        
        
        if existe:
            #Obtener el técnico actual y estado del ticket en la base de datos
            command_F = "SELECT tecnico_id, estado FROM tickets WHERE id_ticket = %s"
            cursor.execute(command_F, (id_ticket,))
            result = cursor.fetchone()
            tecnico_actual, estado_actual = result[0], result[1]

            #Normalizar los nombres de los técnicos para comparar 
            tecnico_normalizado = normalizar_nombre(tecnico_i)
            tecnico_actual_nombre = next(
                (normalizar_nombre(t[1]) for t in tecnicos if str(t[0]) == str(tecnico_actual)), ""
            )

            cambios = False #Indica si hubo cambios
            
            #Si el técnico cambió y no es 'nan' ni 'Sin asignar', se actualiza
            if tecnico_i != 'nan' and tecnico_normalizado != tecnico_actual_nombre and tecnico_i != 'Sin asignar' :
                for t in tecnicos:
                    if tecnico_i == t[1]: #Buscar técnico en base de datos
                        tecnico_i = obtener_id_tecnico(tecnico_i)
                        cambios = True

            #Si el estado cambió, se marca como cambio
            if estado != estado_actual:
                cambios = True

            #Si hubo cambios, actualiza ticket en base de datos
            if cambios:
                try:
                    command = """
                        UPDATE tickets
                        SET tecnico_id = %s, estado = %s
                        WHERE id_ticket = %s
                    """
                    cursor.execute(command, (tecnico_i, estado, id_ticket))
                    connection.commit()
                    break
                except Exception as e:
                    print(e)
        else:
            #Se asigna técnico default si no hay tecnico en la fila
            if tecnico_i == "nan":
                tecnico_i = '1'
            else:
                #Buscar técnico en vase de datos
                for t in tecnicos:
                    if str(t[1]) == str(tecnico_i):
                        tecnico_i = obtener_id_tecnico(tecnico_i)
                        break
                else:
                    #Si no se encuentra se coloca valor por defecto
                    tecnico_i = '1'
            
            #Intentar insertar un nuevo ticket en base de datos
            try:
                command = """
                INSERT INTO tickets(id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
                prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, script_id, observaciones, revisado)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                """
                cursor.execute(command, (id_ticket,titulo,estado,fecha_apertura,fecha_limite,categoria,prioridad,solicitante,localizacion, tecnico_i, '5', '54', observacion, revisado))
                connection.commit()
                
                nuevos +=1 #Incrementa contador de tickets insertados
            except Exception as e:
                print(e)

    #Mostrar mensaje de exito con la cantidad de registros procesados
    if actualizados > 0 and nuevos > 0 or actualizados == 0:
        messagebox.showinfo('Subida completada', f"Se cargaron correctamente {nuevos} registros nuevos")
    elif actualizados > 0 and nuevos == 0:
        messagebox.showinfo('Subida completada', f"No se cargó ningún registro nuevo")
    
    #Actualizar interfaz con los datos de la base de datos
    mostrar_datos(query_datos(), tabla)