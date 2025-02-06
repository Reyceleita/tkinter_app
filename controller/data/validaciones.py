import datetime

def validar_fecha(fecha_entrada):
    try:
        fecha = datetime.datetime.strptime(fecha_entrada, "%Y-%m-%d")
        return True
    except:
        return False