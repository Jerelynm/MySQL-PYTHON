import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python_tarea',
)

cursor= conexion.cursor()
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

print(resultados)

cursor.close()
conexion.close()