import psycopg2
from configuracion.config import config

def decrementar_precio(modelo):
    try:
        # Configuración de la conexión a la base de datos
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Comenzamos una transacción
        conn.autocommit = False

        # Verificamos si el modelo existe en la tabla Producto
        cur.execute("SELECT COUNT(*) FROM Producto WHERE modelo = %s", (modelo,))
        producto_count = cur.fetchone()[0]

        if producto_count > 0:
            # Si el modelo existe en la tabla Producto, decrementamos el precio en $100.00
            cur.execute("UPDATE PC SET precio = precio - 100.00 WHERE modelo = %s", (modelo,))
            print("Precio decrementado en $100.00")

        if producto_count == 0:
            # Si el modelo no existe en la tabla Producto, imprimimos un mensaje indicando que no existe
            print("El modelo especificado no existe")

        # Hacemos un commit para confirmar los cambios
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        # Si ocurre un error, hacemos un rollback para deshacer los cambios
        conn.rollback()

    finally:
        # Cerramos la conexión a la base de datos
        if conn is not None:
            cur.close()
            conn.close()