import os
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from mongoengine import connect

flask_bcrypt = Bcrypt()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config_by_name = dict(
    dev=DevelopmentConfig
)

key = Config.SECRET_KEY

def create_app(config_name):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app=app, supports_credentials=True)
    flask_bcrypt.init_app(app)
    DB_URI = os.getenv('DB_URI', '')
    connect(host=DB_URI)

    return app