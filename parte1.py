import mysql.connector

conexion =mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tarea1"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

cursor.close()
conexion.close()