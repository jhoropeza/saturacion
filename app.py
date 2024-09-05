import os
from flask import Flask, render_template

app = Flask(__name__)

# Obtener la ruta del directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Asegurarte de que Flask busque en la carpeta 'templates' correcta
app.template_folder = os.path.join(ruta_script, 'templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/script1.py', methods=['POST'])
def script1():
    # Aquí va tu código Python para el script 1
    return "Script 1 ejecutado!"

@app.route('/script2.py', methods=['POST'])
def script2():
    # Aquí va tu código Python para el script 2
    return "Script 2 ejecutado!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
