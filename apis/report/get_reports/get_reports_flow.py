from flask import jsonify
from models.report import Report


class GetReportsFlow:

    def __call__(self):
        reports_list = Report.objects()
        reports_jsons_list = []
        reports_jsons_list = list(map(lambda report_obj: report_obj.to_json(), reports_list))

        return jsonify({"reports": reports_jsons_list})

