from flask import jsonify
from models.report import Report
from utils.utils import json_message_error_code


class GetReportByPetIdFlow:
    def __call__(self, request):

        pet_id = request.args.get('pet_id')

        report_obj = Report.objects(
            pet_id=pet_id
        ).first()

        if report_obj is None:
            return json_message_error_code("Reporte no encontrado")

        return jsonify({"report": report_obj.to_json()})
