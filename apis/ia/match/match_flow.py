from utils.utils import jsonify


class MatchFlow:

    def __call__(self, request):
        # Flujo de IA
        reference = request.form["reference"]
        img_from_user = request.form["img_from_user"]


        return jsonify({
            "percentage": "80%"
        })
