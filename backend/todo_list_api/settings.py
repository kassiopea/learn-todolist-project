from datetime import timedelta
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.dev.env'))

SECRET_KEY = environ.get('SECRET_KEY')
MONGO_URI = environ.get('DATABASE_URI')

JWT_COOKIE_SECURE = False
JWT_TOKEN_LOCATION = ['cookies']
JWT_SECRET_KEY = environ.get('SECRET_KEY')
ACCESS_EXPIRES = timedelta(hours=1)
JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
JWT_COOKIE_CSRF_PROTECT = True
JWT_ACCESS_CSRF_HEADER_NAME = "X-CSRF-TOKEN-ACCESS"
JWT_ACCESS_COOKIE_NAME = "access_token"
JWT_BLACKLIST_ENABLED = True
