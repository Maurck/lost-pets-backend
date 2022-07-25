from flask import request
from apis.ia.match.match import Match


def create_routes_match(app):
    
    @app.route('/match', methods=['GET'])
    def match():
        match = Match()
        return match(request)