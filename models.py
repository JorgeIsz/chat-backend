from main import db
from main import login_manager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"<User '{self.username}>"

class Mensaje(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    texto = db.Column(db.String(240),nullable=False)
    estado = db.Column(db.Boolean,default=True)
    room = db.Column(db.String(100),nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()