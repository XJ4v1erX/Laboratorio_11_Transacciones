import psycopg2
from configuracion.config import config
from psycopg2.extras import RealDictCursor

def buscar_pc(velocidad, ram):
    try:
        # Configuración de la conexión a la base de datos
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Comenzamos una transacción
        conn.autocommit = False

        # Buscamos las PCs con la velocidad y RAM especificadas
        cur.execute("SELECT modelo, precio FROM PC WHERE velocidad = %s::float AND ram = %s::integer", (velocidad, ram))
        pcs = cur.fetchall()

        # Hacemos un commit para confirmar los cambios
        conn.commit()

        return pcs

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        # Si ocurre un error, hacemos un rollback para deshacer los cambios
        conn.rollback()

    finally:
        # Cerramos la conexión a la base de datos
        if conn is not None:
            cur.close()
            conn.close() 
