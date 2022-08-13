from flask import request
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