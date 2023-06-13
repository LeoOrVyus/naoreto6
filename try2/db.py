import psycopg2

# Establecer la conexión a la base de datos creada
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="grettel33",
    dbname="urlshortener"
)

# Crear la tabla 'urls' si no existe
create_table_query = """
CREATE TABLE IF NOT EXISTS urls (
    id SERIAL PRIMARY KEY,
    link VARCHAR(100),
    short_url VARCHAR(100) UNIQUE,
    visitors INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

# Ejecutar la consulta para crear la tabla
cursor = conn.cursor()
cursor.execute(create_table_query)

# Confirmar los cambios en la base de datos
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

