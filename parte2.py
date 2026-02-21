import pymysql

conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="tarea1",
    charset='utf8mb4',
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM tabla")
resultados = cursor.fetchall()

conexion.close()