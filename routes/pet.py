'''
pet.py: Modulo para definir las rutas relacionadas con la API Pet
'''
from flask import request
from apis.pet.get_pets.get_pets import GetPets

from apis.pet.register.register_pet import RegisterPet

def create_routes_pet(app):
    '''
    Metodo que crea las rutas relacionadas con la API Pet
    '''
    # pylint: disable=unused-variable
    @app.route('/pet/register', methods=['POST'])
    def register_pet():
        register_pet = RegisterPet()
        return register_pet(request)

    @app.route('/pets', methods=['GET'])
    def get_pets():
        get_pets = GetPets()
        return get_pets(request)
