from flask import request
from apis.report.get_reported_pets.get_reported_pets import GetReportedPets
from apis.report.report_pet.report_pet import ReportPet

def create_routes_report(app):
    '''
    Metodo que crea las rutas relacionadas con la API Report
    '''
    # pylint: disable=unused-variable
    @app.route('/report', methods=['POST'])
    def report_pet():
        report_pet = ReportPet()
        return report_pet(request)

    @app.route('/report/pets')
    def get_reported_pets():
        get_reported_pets = GetReportedPets()
        return get_reported_pets(request)