# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return'''<h1>¡Hola desde mi Web App de Python 3.11 en Azure App Service!</h1>
    <br><h2>Youtube: OX I Jonatan</h2>
    <br><img src="/static/maxresdefault (3).jpg" width="50%" height="50%" alt="Thumbnail 1">
    <br>
    <br><img src="/static/maxresdefault (4).jpg" width="50%" height="50%" alt="Thumbnail 2">
    <br><h2>Github: JonatanPlancarte960</h2>
    '''

if __name__ == '__main__':
    app.run()