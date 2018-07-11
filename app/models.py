from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String(32), index=True, unique=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(16), index=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    population = db.Column(db.Integer)

