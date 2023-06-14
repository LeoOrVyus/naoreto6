from flask import Flask, request, redirect, render_template
import string
import random
import psycopg2

app = Flask(__name__)

def generate_short_url():
    """Generar una cadena de URL corta aleatoria."""
    chars = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(chars) for _ in range(6))
        cursor = conn.cursor()
        cursor.execute("SELECT short_url FROM urls WHERE short_url = %s", (short_url,))
        if not cursor.fetchone():
            cursor.close()
            return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Manejar el envío del formulario
        url = request.form['url']
        short_url = generate_short_url()
        
        # Insertar datos en la tabla 'urls'
        insert_query = "INSERT INTO urls (link, short_url) VALUES (%s, %s)"
        values = (url, short_url)
        
        cursor = conn.cursor()
        cursor.execute(insert_query, values)
        conn.commit()
        
        return render_template('index.html', short_url=short_url)
    else:
        # Mostrar el formulario
        return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redirigir la URL corta a la URL original."""
    select_query = "SELECT link FROM urls WHERE short_url = %s"
    values = (short_url,)
    
    cursor = conn.cursor()
    cursor.execute(select_query, values)
    result = cursor.fetchone()
    
    if result:
        url = result[0]
        cursor.close()
        
        # Actualizar el contador de visitantes
        update_query = "UPDATE urls SET visitors = visitors + 1 WHERE short_url = %s"
        cursor = conn.cursor()
        cursor.execute(update_query, values)
        conn.commit()
        
        return redirect(url)
    else:
        return "Lo siento, no se pudo encontrar esa URL."

if __name__ == '__main__':
    # Establecer la conexión a la base de datos
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="grettel33",
        dbname="urlshortener"
    )
    app.run(debug=True)
