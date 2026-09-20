import os
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Definimos la ruta completa de la carpeta de subidas dentro de app/static
UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    title = request.form.get('title')
    file = request.files.get('image')

    if file:
        # Crea la carpeta 'uploads' automáticamente si no existe
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Optimización de la imagen con Pillow
        img = Image.open(filepath)
        optimized_filename = 'opt_' + file.filename
        optimized_path = os.path.join(app.config['UPLOAD_FOLDER'], optimized_filename)
        
        # Redimensionar y guardar con compresión
        img.save(optimized_path, optimize=True, quality=60)

        return render_template('result.html', title=title, original=file.filename, optimized=optimized_filename)

if __name__ == '__main__':
    app.run(debug=True)