import mysql.connector
from mysql.connector import Error

conexion = None
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='python_tarea',)
    if conexion.is_connected():
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()
        print(f"Base de datos actual: {db[0]}")

except Error as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    if conexion is not None and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada")