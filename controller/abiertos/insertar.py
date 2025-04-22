from model.connection import *
import datetime


# Subir a base de datos nuevos tickets abiertos
def insertar_abierto(
    id_ticket,
    titulo,
    estado,
    fecha_apertura,
    fecha_limite,
    categoria,
    prioridad,
    solicitante,
    localizacion,
    tecnico_i,
    observacion,
    estado_t,
    revisado,
):
    
    script_id = get_id_script_sin_asignar()
    connection = connection_to_db()
    cursor = connection.cursor()
    command = """
    INSERT INTO tickets_diarios(
        id_ticket, titulo, estado, fecha_apertura, fecha_limite, categoria, 
        prioridad, solicitante, localizacion, tecnico_id, forma_solucion_id, 
        script_id, observaciones, fecha_actualiza, estado_t, revisado
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %X")
    cursor.execute(
        command,
        (
            id_ticket,
            titulo,
            estado,
            fecha_apertura,
            fecha_limite,
            categoria,
            prioridad,
            solicitante,
            localizacion,
            tecnico_i,
            "5",
            script_id,
            observacion,
            fecha_actual,
            estado_t,
            revisado,
        ),
    )
    connection.commit()

def get_id_script_sin_asignar():
    conn = connection_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id_script FROM scripts WHERE script = 'Sin asignar'")
    result = cursor.fetchone()
    return result[0] if result else None
