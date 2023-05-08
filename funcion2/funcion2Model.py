
import psycopg2
from configuracion.config import config

def eliminar_modelo(modelo):
    try:
        # Configuración de la conexión a la base de datos
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Comenzamos una transacción
        conn.autocommit = False

        # Verificamos si el modelo existe en la tabla PC
        cur.execute("SELECT COUNT(*) FROM PC WHERE modelo = %s", (modelo,))
        pc_count = cur.fetchone()[0]

        if pc_count > 0:
            # Si el modelo existe en la tabla PC, eliminamos la tupla correspondiente
            cur.execute("DELETE FROM PC WHERE modelo = %s", (modelo,))
            print("Tupla eliminada de la tabla PC")

        # Verificamos si el modelo existe en la tabla Producto
        cur.execute("SELECT COUNT(*) FROM Producto WHERE modelo = %s", (modelo,))
        producto_count = cur.fetchone()[0]

        if producto_count > 0:
            # Si el modelo existe en la tabla Producto, eliminamos la tupla correspondiente
            cur.execute("DELETE FROM Producto WHERE modelo = %s", (modelo,))
            print("Tupla eliminada de la tabla Producto")

        if pc_count == 0 and producto_count == 0:
            # Si el modelo no existe en ninguna de las dos tablas, imprimimos un mensaje indicando que no existe
            print("El modelo especificado no existe")
            
        # Hacemos un commit para confirmar los cambios
        conn.commit()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        # Si ocurre un error, hacemos un rollback para deshacer los cambios
        conn.rollback("Error al eliminar la tupla")

    finally:
        # Cerramos la conexión a la base de datos
        if conn is not None:
            cur.close()
            conn.close()