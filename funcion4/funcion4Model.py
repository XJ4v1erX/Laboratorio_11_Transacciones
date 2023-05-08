import psycopg2
from configuracion.config import config


def buscar_o_insertar_pc(fabricante, modelo, velocidad, ram, disco, precio):
    try:
        # Configuración de la conexión a la base de datos
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Comenzamos una transacción
        conn.autocommit = False

        # Buscamos si hay una PC que cumpla con las características especificadas
        cur.execute("""SELECT COUNT(*) FROM PC p
                        JOIN Producto pr ON p.modelo = pr.modelo
                        WHERE pr.fabricante = %s AND p.modelo = %s 
                        AND p.velocidad = %s AND p.ram = %s 
                        AND p.disco = %s AND p.precio = %s""",
                    (fabricante, modelo, velocidad, ram, disco, precio))
        pc_count = cur.fetchone()[0]

        if pc_count > 0:
            # Si se encuentra un modelo con las características especificadas, mostramos un mensaje de error al usuario
            print("Ya existe una PC con esas características")

        else:
            # Si no se encuentra un modelo con las características especificadas, lo insertamos en las tablas Producto y PC
            cur.execute("INSERT INTO Producto(fabricante,modelo, tipo) VALUES (%s,%s, 'PC')", (fabricante,modelo))
            cur.execute("INSERT INTO PC(modelo, velocidad, ram, disco, precio) VALUES (%s, %s, %s, %s, %s)", (modelo, velocidad, ram, disco, precio))
            print("Se ha insertado la PC con éxito")

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