# Cargar datos seleccionados en la tabla seleccionada
def mostrar_datos(datos, tabla):

    for row in tabla.get_children():
        tabla.delete(row)

    incompleto = []
    conteo = 0
    for row in datos:
        conteo += 1
        incompleto = [(campo if campo is not None else "Sin definir") for campo in row]
        tabla.insert("", "end", values=list(incompleto))

    return conteo


# Organizar valores de la columna
def ordenar_tabla(tabla, col, descendiente, columnas):
    data = [(tabla.set(item, col), item) for item in tabla.get_children("")]
    data.sort(reverse=descendiente)
    column = col
    for columna in columnas:
        tabla.heading(columna, text=columna)
        if descendiente:
            tabla.heading(col, text=f"{column} ▼")
        else:
            tabla.heading(col, text=f"{column} ▲")

    for index, (val, item) in enumerate(data):
        tabla.move(item, "", index)
    tabla.heading(
        col, command=lambda: ordenar_tabla(tabla, col, not descendiente, columnas)
    )
