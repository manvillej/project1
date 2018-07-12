from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    checkins = db.relationship("CheckIn", backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String(32), index=True, unique=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(16), index=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    population = db.Column(db.Integer)
    checkins = db.relationship("CheckIn", backref="location", lazy=True)

    def __repr__(self):
        return f'<Location - ({self.longitude}, {self.latitude}), ({self.city}, {self.state} {self.zipcode})>'.format()

class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    body = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __repr__(self):
        return f'<CheckIn {self.user_id}, {self.location_id}>'