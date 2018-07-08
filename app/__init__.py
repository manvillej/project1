from flask import Flask
from config import Config, site_config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

app = Flask(__name__)
app.config.from_object(Config)
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


from app import routes
