from flask import request
from apis.report.delete_report.delete_report import DeleteReport
from apis.report.get_reported_pets.get_reported_pets import GetReportedPets
from apis.report.get_reports.get_reports import GetReports
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

    @app.route('/reports')
    def get_reports():
        get_reports = GetReports()
        return get_reports(request)

    @app.route('/report', methods=['DELETE'])
    def delete_report():
        delete_report = DeleteReport()
        return delete_report(request)