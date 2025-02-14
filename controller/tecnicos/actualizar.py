from tkinter import  messagebox

from controller.data.obtener_data import *
from controller.tecnicos.consultar import *
from controller.data.validaciones import *


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
    id_tecnico = id_tecnico
    cargo = obtener_cargo(cargo_id ,cargo_edit)
    if validar_fecha(fecha_i_editar) and validar_fecha(fecha_s_editar):
        if nombre_edit.strip() != "" and cargo is not None:
            nombre = nombre_edit
            fecha_inicio = str(fecha_i_editar)
            fecha_fin = str(fecha_s_editar)
            command = """
                UPDATE tecnicos
                SET nombre = %s, cargo_id = %s, fecha_ingreso = %s, fecha_salida = %s
                WHERE id_tecnico = %s
            """
            cursor.execute(command, (nombre, cargo, fecha_inicio, fecha_fin, id_tecnico))
            connection.commit()
            editar.destroy()
            cargar_tecnicos(tabla)
        else:
            messagebox.showerror('Error', 'Complete todos los campos')
            editar.lift()
    else:
        messagebox.showerror('Error', 'Fecha inválida \nFormato correcto: YYYY-MM-DD')
        editar.lift()

