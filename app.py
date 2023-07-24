# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola desde mi Web App de Python 3.11 en Azure App Service!'

if __name__ == '__main__':
    app.run()