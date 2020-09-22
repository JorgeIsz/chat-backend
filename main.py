from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

import models

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Hello World!"

mensajes = []

@socketio.on('message')
def handleMessage(msg):
    respuesta = {
        'texto':msg['texto'],
        'usuario':msg['usuario']
    }
    mensajes.append(respuesta)
    emit('message', mensajes,broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host="localhost",debug=True)