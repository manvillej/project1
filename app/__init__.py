from flask import Flask
from config import Config, site_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
