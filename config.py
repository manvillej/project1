import os

class Config(object):
	# Check for environment variable
	if not os.getenv("DATABASE_URL"):
	    raise RuntimeError("DATABASE_URL is not set")
	SESSION_PERMANENT = False
	SESSION_TYPE = "filesystem"

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	#if not os.getenv("SECRET_KEY"):
	#	raise RuntimeError("SECRET_KEY is not set")

	
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False