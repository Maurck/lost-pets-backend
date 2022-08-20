import cloudinary.uploader
from models.pet import Pet
from models.report import Report
from utils.utils import json_message, json_message_error_code 


class DeleteReportFlow:

    def __call__(self, request):
        report_id = request.args.get('id')    
        report: Report = Report.objects(
            id=report_id
        ).first()

        if report is None:
            return json_message_error_code("Reporte no encontrado")

        pet: Pet = Pet.objects(
            id=report.to_json()["pet_id"]
        ).first()

        if pet is not None:
            pet.is_reported = False
            pet.save()

        cloudinary.uploader.destroy(report.to_json()["reported_img_public_id"])
        report.delete()

        return json_message("Reporte borrado")
