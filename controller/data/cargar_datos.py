import pandas as pd
from tkinter import filedialog, messagebox

def cargar_datos():
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
                return reporte
            except Exception as e:
                print(f"Error: {e}")
        except Exception as e:
            messagebox.showwarning('Advertencia', f'No se pudo cargar el archivo \nArchivo no válido, solo se admiten arcivos .csv')
            print(e)