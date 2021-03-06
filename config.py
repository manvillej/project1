import os
from app.siteConfig import SiteConfig


class Config(object):
    # Check for environment variable
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    if not os.getenv("DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not set")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    API_KEY = os.environ.get('API_KEY') or 'you-will-never-guess'


site_config = SiteConfig(
    brand='Manville',
    project_url='https://github.com/manvillej/project1',
    github_url='https://github.com/manvillej',
    social_url='https://twitter.com/JeffManville',
    )
