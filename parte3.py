import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tarea1"
    )

    if conexion.is_connected():
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE();")
        db=cursor.fetchone()
        print("Base de datos: {db}")

except Error as e:
    print(f"Error: {e}")

finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada")