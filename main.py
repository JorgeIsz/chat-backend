from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
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

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    respuesta = {
        'tipo':'alerta',
        'mensaje':username + ' has entered the room ' + room
    }
    send(respuesta, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

@socketio.on('message')
def handleMessage(msg):
    respuesta = {
        'texto':msg['texto'],
        'usuario':msg['usuario']
    }
    mensajes.append(respuesta)
    emit('message', mensajes,broadcast=True,room="testroom")

if __name__ == '__main__':
    socketio.run(app,host="localhost",debug=True)