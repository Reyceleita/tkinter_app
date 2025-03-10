from model.connection import *




#Funcón para obtener id del tecnico según nombre, en caso de no existir se coloca sin asignar
def obtener_id_tecnico(nombre):
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT id_tecnico FROM tecnicos WHERE nombre = ?', (nombre, ))
    tecnico = cursor.fetchone()
    return str(tecnico[0]) if tecnico else '1'

#Función para obtener información de un ticket por su id
def obtener_ticket_abierto(ticket):
    connection = connection_to_db()
    cursor = connection.cursor()
    command = """
        SELECT tecnico_id, estado, fecha_actualiza, revisado 
        FROM tickets_diarios 
        WHERE id_ticket = ?
    """
    cursor.execute(command, (ticket, ))
    ticket = cursor.fetchone()
    return ticket

#Función para obtener el estado de un ticket abierto
def obtener_estado(ticket):
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT estado_t FROM tickets_diarios WHERE id_ticket = ?', (ticket, ))
    estado = cursor.fetchone()
    estado = estado[0]
    return estado

#Función para obtener las soluciones de base de datos
def cargar_solucion(solucion, solucion_list):
    connection = connection_to_db()
    cursor = connection.cursor()
    solucion['values'] = []
    solucion_list.clear()
    
    command = "SELECT id_solucion, solucion FROM forma_solucion"
    cursor.execute(command)
    soluciones = cursor.fetchall()
    for id_solucion, solucion_ in soluciones:
        solucion_list[solucion_] = id_solucion
        solucion['values'] = list(solucion_list.keys())

#Función para obtener los scripts de base de datos
def cargar_script(script, script_list):
    connection = connection_to_db()
    cursor = connection.cursor()
    script['values'] = []
    script_list.clear()
    
    command = "SELECT id_script, script FROM scripts"
    cursor.execute(command)
    scripts = cursor.fetchall()
    for id_script, script_ in scripts:
        script_list[script_] = id_script
        script['values'] = list(script_list.keys())

#Función para obtener los técnicos de base de datos
def cargar_tecnico(tecnico, tecnico_list):
    connection = connection_to_db()
    cursor = connection.cursor()
    tecnico['values'] = []
    tecnico_list.clear()
    
    command = "SELECT id_tecnico, nombre FROM tecnicos"
    cursor.execute(command)
    tecnicos = cursor.fetchall()
    
    for id_tecnico, tecnico_ in tecnicos:
        tecnico_list[tecnico_] = id_tecnico
        tecnico['values'] = list(tecnico_list.keys())

#Obtener datos de tablas específicas
def cargar_tablas(datos, tabla_list, tabla):
    connection = connection_to_db()
    cursor = connection.cursor()
    datos.set('')
    datos['values'] = []
    tabla_list.clear()
    
    command = f"SELECT * FROM {tabla}"
    cursor.execute(command)
    tecnicos = cursor.fetchall()
    
    for id_dato, dato_ in tecnicos:
        tabla_list[dato_] = id_dato
        datos['values'] = list(tabla_list.keys())

#Obtener las observaciones de base de datos 
def cargar_observacion(tabla, id):
    connection = connection_to_db()
    cursor = connection.cursor()
    command = f"SELECT observaciones FROM {tabla} WHERE id_ticket = ?"
    cursor.execute(command, (id, ))
    obsesrvacion = cursor.fetchone()
    return obsesrvacion[0]

#Función para obtener el id de un combobox
def obtener_campo_lista(lista, menu):
    id = menu
    if id in lista:
        id_obtenido = lista[id]
        return id_obtenido

#Función para obtener el id de un combobox
def obtener_cargo(cargo_id, combobox):
    cargo = combobox
    if cargo in cargo_id:
        id_cargo = cargo_id[cargo]
        return id_cargo

#Obtener listado de cargos
def cargar_cargo(cargo_id, combobox):
    connection = connection_to_db()
    cursor = connection.cursor()
    combobox['values'] = []
    cargo_id.clear()

    command = "SELECT id_cargo, cargo FROM cargos"
    cursor.execute(command)
    cargos = cursor.fetchall()
    for id_cargo, cargo in cargos:
        cargo_id[cargo] = id_cargo
        combobox['values'] = list(cargo_id.keys())