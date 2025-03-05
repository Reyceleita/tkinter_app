from controller.data.obtener_data import *
from controller.tecnicos.consultar import *
from controller.data.validaciones import *
from view.alertas.error import *
from view.alertas.warning import *
from logs.logger_config import logger

def actualizar_tecnico(id_tecnico, cargo_edit, fecha_i_editar, fecha_s_editar, nombre_edit, editar, cargo_id, tabla):
    """
    Actualizar datos de un técnico.
    Parámetros:

        id_tecnico (tk.StringVar): Id del tecnico a modificar
        cargo_edit (ttk.Combobx): Campo del formulario
        fecha_i_editar (ttk.Entry): Campo del formulario
        fecha_s_editar (tt.Erntry): Campo del formulario
        nombre_edit (ttk.Etry): Campo del formulario
        editar (tk.TopLevel): Campo del formulario
        cargo_id (List): Lista de cargos
        tabla (ttk.TreeView): Tabla de técnicos
    Resuoltados: 
        Se cambia el técnico en base de datos y recarga la tabla
    """
    try:
        id_tecnico = id_tecnico
        cargo = obtener_cargo(cargo_id ,cargo_edit)
        if validar_fecha(fecha_i_editar) and validar_fecha(fecha_s_editar):
            if nombre_edit.strip() != "" and cargo is not None:
                nombre = nombre_edit
                fecha_inicio = str(fecha_i_editar)
                fecha_fin = str(fecha_s_editar)
                command = """
                    UPDATE tecnicos
                    SET nombre = ?, cargo_id = ?, fecha_ingreso = ?, fecha_salida = ?
                    WHERE id_tecnico = ?
                """
                cursor.execute(command, (nombre, cargo, fecha_inicio, fecha_fin, id_tecnico))
                connection.commit()
                editar.destroy()
                cargar_tecnicos(tabla)
            else:
                AdverteciaAlerta(editar, 'Complete todos los campos')
                editar.lift()
        else:
            AdverteciaAlerta(editar, 'Fecha inválida \nFormato correcto: YYYY-MM-DD')
            editar.lift()
    except Exception as e:
        logger('o se logró actualizar el tecnico %s', e)
        ErrorAlert(editar, 'Error al actualizar el técnico')

