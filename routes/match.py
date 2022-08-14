from flask import request
from apis.ia.match.match import Match
from apis.ia.breed.breed import Breed

def create_routes_match(app):
    
    @app.route('/match', methods=['GET'])
    def match():
        match = Match()
        return match(request)


    @app.route('/breed', methods=['GET'])
    def breed():
        breed = Breed()
        return breed(request)