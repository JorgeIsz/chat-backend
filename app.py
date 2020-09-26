from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from serializers.mensaje_serializer import MensajeSerializerFactory 

msg_srlr = MensajeSerializerFactory()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app, cors_allowed_origins="*")

class Mensaje(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    texto = db.Column(db.String(240),nullable=False)
    estado = db.Column(db.Boolean,default=True)
    room = db.Column(db.String(100),nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

@app.route('/')
def index():
    return "Hello World!"

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


@socketio.on('mensaje-entra')
def on_mensaje_entra(msg):
    nuevo_mensaje = Mensaje(
        texto = msg['texto'],
        room = msg['room']
        )
    nuevo_mensaje.save()
    mensajes = Mensaje.query.all()
    serializer = msg_srlr.get_serializer(True)

    send(serializer.data(mensajes), room=msg["room"])

@socketio.on('estado-cambiado')
def on_estado_cambiado(data):
    print("Cambiar",data)
    usuario = data["usuario"]
    estado = data["estado"]
    room = data["room"]
    respuesta = {
        'tipo':'alerta',
        'estado':estado,
        'usuario':usuario
    }
    send(respuesta,room=room)



if __name__ == '__main__':
    socketio.run(app,debug=True)