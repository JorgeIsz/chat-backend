from main import db
from main import login_manager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"<User '{self.username}>"