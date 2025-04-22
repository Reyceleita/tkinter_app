import sqlite3
from model.connection import connection_to_db


# Script para base de datos en sqlite
def crear_tablas_db():
    try:
        with connection_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS cargos (
                id_cargo INTEGER PRIMARY KEY AUTOINCREMENT,
                cargo TEXT
            );
                """
            )

            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS tecnicos (
                id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                cargo_id INTEGER,
                fecha_ingreso TEXT,
                fecha_salida TEXT
            );
                """
            )

            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS forma_solucion (
                id_solucion INTEGER PRIMARY KEY AUTOINCREMENT,
                solucion TEXT
            );
                """
            )

            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS scripts (
                id_script INTEGER PRIMARY KEY AUTOINCREMENT,
                script TEXT
            );
                """
            )

            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS tickets (
                id_ticket INTEGER PRIMARY KEY ,
                titulo TEXT,
                estado TEXT,
                fecha_apertura TEXT,
                fecha_limite TEXT,
                categoria TEXT,
                prioridad TEXT,
                solicitante TEXT,
                localizacion TEXT,
                tecnico_id INTEGER,
                forma_solucion_id INTEGER,
                script_id INTEGER,
                fecha_solucion TEXT,
                observaciones TEXT,
                revisado TEXT,
                FOREIGN KEY (tecnico_id) REFERENCES tecnicos(id_tecnico),
                FOREIGN KEY (forma_solucion_id) REFERENCES forma_solucion(id_solucion),
                FOREIGN KEY (script_id) REFERENCES scripts(id_script)
            );
                """
            )

            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS tickets_diarios (
                id_ticket INTEGER PRIMARY KEY ,
                titulo TEXT,
                estado TEXT,
                fecha_apertura TEXT,
                fecha_limite TEXT,
                categoria TEXT,
                prioridad TEXT,
                solicitante TEXT,
                localizacion TEXT,
                tecnico_id INTEGER,
                forma_solucion_id INTEGER,
                script_id INTEGER,
                fecha_solucion TEXT,
                observaciones TEXT,
                fecha_actualiza TEXT,
                estado_t TEXT,
                revisado TEXT,
                FOREIGN KEY (tecnico_id) REFERENCES tecnicos(id_tecnico),
                FOREIGN KEY (forma_solucion_id) REFERENCES forma_solucion(id_solucion),
                FOREIGN KEY (script_id) REFERENCES scripts(id_script)
            );
                """
            )

            cursor.execute(
                """
            INSERT INTO cargos(cargo)
            Values
            ('N/A'),
            ('DEV'),
            ('LT'),
            ('AD'),
            ('QA');
                """
            )

            cursor.execute(
                """
            INSERT INTO forma_solucion(solucion)
            Values
            ('Consulta BD'),
            ('Script BD'),
            ('Informe'),
            ('No aplica'),
            ('Sin asignar');
                """
            )

            cursor.execute(
                """
            INSERT INTO tecnicos('nombre', 'cargo_id')
            VALUES
            ('Sin asignar', '1'),
            ('Santiago Ñustes', '2'),
            ('Juan Camilo Figueroa', '5'),
            ('Juan David Becerra Molano', '2'),
            ('Camilo Ospina Escudero', '5'),
            ('Laura Natalia Forero Artunduaga', '3'),
            ('Juan Pablo Alfonso Beltran', '2'),
            ('Jairo Esteban Rodriguez Jimenez', '2'),
            ('Miguel Angel Pardo Reyes', '2'),
            ('Faiver Leguizamo Rojas', '4'),
            ('Edgar Yesid Cortes Insuasty', '3'),
            ('Jairo Miller Urrego Garay', '2'),
            ('Mauricio Enrique Hernandez Cabrera', 2),
            ('German Orlando Ramirez Sarmiento', 2),
            ('Diosenelth de la Hoz Fonseca', 2),
            ('Jimmy Alexander Menjura Calvo', 2);
                """
            )

            cursor.execute(
                """
            INSERT INTO scripts(script)
            Values
            ('Actualiza Centro Servicio'),
            ('Actualiza comprobante caja'),
            ('Actualiza datos Canal de Venta'),
            ('Actualiza datos pre envío'),
            ('Actualiza Guía'),
            ('Actualiza Guía Notificaciones'),
            ('Actualiza IDEstadoGuia'),
            ('Actualiza Lista Precios'),
            ('Actualiza Localidad Estado'),
            ('Actualiza Motivo'),
            ('Actualiza parámetros para pago'),
            ('Actualiza Planilla Asignación Mensajero'),
            ('Actualiza planilla comprobante caja'),
            ('Actualiza zonas difícil acceso'),
            ('Actualización Fecha Entrega'),
            ('Actualizar datos cliente frecuente'),
            ('Actualizar Fecha Estimada en Años'),
            ('Actualizar microzonas'),
            ('Actualizar usuario interno'),
            ('Actualizar usuario portal'),
            ('Agrupación Factura'),
            ('Cambio de estado'),
            ('Cambio Estado planilla'),
            ('Causación manual'),
            ('Condonar Listas Restrictivas'),
            ('Consulta a base de datos'),
            ('Creación de SACAS'),
            ('Delete descargue mensajero anterior'),
            ('Elimina archivos digitalización'),
            ('Eliminar Cliente Frecuente'),
            ('Eliminar huella tercero'),
            ('Eliminar recibido'),
            ('Eliminar usuario portal'),
            ('Eliminar Datos Usuario'),
            ('EliminaTrazaGuía'),
            ('Insertar Actualizar clave usuario'),
            ('Insertar Agencia APP'),
            ('Insertar Cajas al CS'),
            ('Insertar Causal'),
            ('Insertar Centros Penitenciarios'),
            ('Insertar Controller masivo SAC'),
            ('Insertar Corresponsal Inegocio'),
            ('Insertar Guías a Custodia'),
            ('Insertar Provision Suministro'),
            ('Liquidación PAMI'),
            ('Movimiento de bodega / inventario'),
            ('Reactivación manual para pago'),
            ('Retirar check de cancelado'),
            ('Usuario null'),
            ('Reiniciar reintentos'),
            ('Actualiza limite de texto'),
            ('No aplica'),
            ('Sin asignar');
                """
            )

            cursor.execute(
                "CREATE TABLE IF NOT EXISTS execution_log (executed INTEGER)"
                )

            connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error al insertar en la base de datos: {e}")
    except KeyError as e:
        print(f"Clave faltante en el elemento: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
