'''Archivo que ejecuta la aplicacion'''
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from config.config import server_config
from config.config import get_app
from config.config import run_app
from routes.match import create_routes_match
from routes.pet import create_routes_pet
from routes.user import create_routes_user

app = get_app(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

server_config(app)

@app.get('/')
def index():
    return 'Hola Mundo'

create_routes_user(app, bcrypt)
create_routes_pet(app)
create_routes_match(app)

if __name__ == '__main__':
    run_app(app)
