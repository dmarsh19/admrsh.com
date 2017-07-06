from flask_restful import Resource

from admrsh import api
from .models import AtmoReading


class AtmoReadings(Resource):
    def get(self):
        return [a.as_dict() for a in AtmoReading.query.all()]


api.add_resource(AtmoReadings, '/atmo', endpoint='atmo')
