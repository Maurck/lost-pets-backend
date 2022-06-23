from flask_restx import Api
from flask import Blueprint

from .user.user_controller import user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='App para mascotas perdidas',
          version='1.0',
          description='Esta es una app que permite encontrar las mascotas perdidas',
          doc='/api/docs',
          validate=True
          )

api.add_namespace(user_ns, path='/user')