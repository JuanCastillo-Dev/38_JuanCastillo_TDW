from flask import Flask, render_template  # Creacion de la app

app = Flask(__name__)

@app.route('/')  # La pagina principal direcciona a la raiz
def index():
    return render_template('index.html')  # Mostrar el html

if __name__ == '__main__':
    app.run(debug=True)  # Inicia el servidor