import pandas as pd
from tkinter import filedialog, messagebox
from view.alertas.error import *

def cargar_datos(frame):
    """
    Leer archivo csv y trnasforma los datos para su manejo
    
    Resultados:
        (Dataframe) reporte: Datos extraidos del archivo csv
    """
    archivo = filedialog.askopenfilename(
        filetypes=[('Archivos CSV', '*.csv'), ('Todos los archivos', '*.*')]
    )
    if archivo:
        try:
            reporte = pd.read_csv(archivo, encoding='utf-8-sig', sep=';', quotechar='"')
            try:
                columnas_renombradas = {
                    'Última actualización': 'UltimaActualizacion',
                    'Fecha de Apertura': 'FechaApertura',
                    'Tiempo de solución': 'TiempoSolucion',
                    'Solicitante - Solicitante': 'Solicitante',
                    'Asignado a: - Técnico': 'TécnicoAsignado',
                    'Asignado a: - Grupo de Tecnicos': 'AsignadoGrupo',
                    'Fecha de cierre': 'FechaCierre',
                    'Fecha de solución': 'FechaSolucion',
                    'Tareas - Fecha Final': 'FechaFinal'
                }
                reporte['ID'] = reporte['ID'].str.replace(' ', '', regex=False)
                reporte.rename(columns=columnas_renombradas, inplace=True)
                reporte = reporte.set_index("ID")
                reporte = reporte.where(pd.notna(reporte), None)
                return reporte
            except Exception as e:
                ErrorAlert(frame, e)
                
        except Exception as e:
            ErrorAlert(frame, e)