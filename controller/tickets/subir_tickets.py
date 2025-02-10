import unicodedata
from tkinter import messagebox

from model.connection import *
from controller.data.obtener_data import *
from controller.data.normalizar import *
from controller.data.cargar_datos import *
from controller.data.mostrar import *
from controller.tickets.consultar import *

connection = connection_to_db()
cursor = connection.cursor()


def subir_tickets(tabla):
    reporte = cargar_datos()
    
    if reporte is None:
        exce = 'Documento vacio'
        return exce
    
    command_R = "SELECT id_ticket FROM tickets;"
    cursor.execute(command_R)
    tickets = cursor.fetchall()
    command_T = "SELECT id_tecnico, nombre, cargo_id FROM tecnicos"
    cursor.execute(command_T)
    tecnicos = list(cursor.fetchall())
    count_r = 0
    count_s = 0
    
    
    for indice, row in reporte.iterrows():
        existe = False
        id_ticket = int(indice)
        titulo = row.values[0]
        estado = row.values[3]
        fecha_apertura = row.values[4]
        fecha_limite = row.values[5]
        categoria = row.values[6]
        prioridad = row.values[7]
        solicitante = row.values[8]
        tecnico_i = str(row.values[9])
        localizacion = row.values[12]
        revisado = "No revisado"
        observacion = " "
        
        for t in tickets:
            if t[0] == id_ticket:
                existe = True
                break
            
        if existe:
            command_F = "SELECT tecnico_id, estado FROM tickets WHERE id_ticket = %s"
            cursor.execute(command_F, (id_ticket,))
            result = cursor.fetchone()
            tecnico_actual, estado_actual = result[0], result[1]

            
            tecnico_normalizado = normalizar_nombre(tecnico_i)
            tecnico_actual_nombre = next(
                (normalizar_nombre(t[1]) for t in tecnicos if str(t[0]) == str(tecnico_actual)), ""
            )

            cambios = False
            if tecnico_i != 'nan' and tecnico_normalizado != tecnico_actual_nombre and tecnico_i != 'Sin asignar' :
                for t in tecnicos:
                    if tecnico_i == t[1]:
                        tecnico_i = obtener_id_tecnico(tecnico_i)
                        cambios = True

            if estado != estado_actual:
                cambios = True

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
            
            if tecnico_i == "nan":
                tecnico_i = '1'
            else:
                for t in tecnicos:
                    if str(t[1]) == str(tecnico_i):
                        tecnico_i = obtener_id_tecnico(tecnico_i)
                        break
                else:
                    tecnico_i = '1'
            
            try:
                command = """
                INSERT INTO tickets(id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
                prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, script_id, observaciones, revisado)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                """
                cursor.execute(command, (id_ticket,titulo,estado,fecha_apertura,fecha_limite,categoria,prioridad,solicitante,localizacion, tecnico_i, '5', '54', observacion, revisado))
                connection.commit()
                
                count_s +=1
            except Exception as e:
                print(e)
                
    if count_r > 0 and count_s > 0 or count_r == 0:
        messagebox.showinfo('Subida completada', f"Se cargaron correctamente {count_s} registros nuevos")
    elif count_r > 0 and count_s == 0:
        messagebox.showinfo('Subida completada', f"No se cargó ningún registro nuevo")
    mostrar_datos(query_datos(), tabla)