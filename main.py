from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Yes!"

mensajes = []
usuarios = 0

@socketio.on('message')
def handleMessage(msg):
    respuesta = {
        'texto':msg['texto'],
        'usuario':msg['usuario']
    }
    mensajes.append(respuesta)
    emit('message', mensajes,broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host="localhost")