from flask import jsonify
from models.pet import Pet
from models.report import Report
from models.user import User
from utils.utils import json_message_error_code
import cloudinary.uploader


class ReportPetFlow:
    '''
    Clase que crea un reporte
    '''
    def __call__(self, request):

        reporter_id = request.form['reporter_id']

        reporter: User = User.objects(
            id=reporter_id
        ).first()

        if reporter is None:
            return json_message_error_code("Usuario que reporta no encontrado")

        pet_id = request.form['pet_id']

        pet: Pet = Pet.objects(
            id=pet_id
        ).first()

        if pet is None:
            return json_message_error_code("Mascota a reportar no encontrada")

        reported_img = request.files['reported_img']
        upload_data = cloudinary.uploader.upload(reported_img)

        new_report = Report(
            address=request.form['address'],
            description=request.form['description'],
            pet_id=pet_id,
            reporter_id=reporter_id,
            reported_img_url=upload_data["url"],
            reported_img_public_id=upload_data["public_id"]
        )

        new_report.save()

        return jsonify({
            "msg": "Reporte creado",
            "report": new_report.to_json()
        })
