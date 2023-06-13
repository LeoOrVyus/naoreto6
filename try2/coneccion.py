import mysql.connector

# Establecer la conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Grettel33",
    database="urlshortener"
)

# Verificar si la conexión fue exitosa
if conn.is_connected():
    print("Conexión exitosa a la base de datos.")
else:
    print("Error al conectar a la base de datos.")

# Cerrar la conexión
conn.close()
