import time

from flask_restful import Resource, reqparse, abort

from admrsh import api
from .models import AtmoRead


query_parser = reqparse.RequestParser()
query_parser.add_argument('startAt', location='args')
query_parser.add_argument('endAt', location='args')


class AtmoReadingList(Resource):
    def get(self):
        args = query_parser.parse_args()
        start = args.pop('startAt', None)
        end = args.pop('endAt', None)
        if start and not end:
            return [a.as_dict() for a in AtmoRead.query.filter(AtmoRead.datetime >= start).all()]
        if not start and end:
            return [a.as_dict() for a in AtmoRead.query.filter(AtmoRead.datetime <= end).all()]
        if start and end:
            if start > end:
                abort(404, message="startAt must be less than endAt")
            else:
                return [a.as_dict() for a in AtmoRead.query.filter(AtmoRead.datetime.between(start, end)).all()]
        return [a.as_dict() for a in AtmoRead.query.all()]
        #return [a.as_dict() for a in AtmoRead.query.order_by(AtmoRead.datetime).all()]


class AtmoReading(Resource):
    def get(self, datetime):
        return AtmoRead.query.filter(AtmoRead.datetime.startswith(datetime)).first_or_404().as_dict()


api.add_resource(AtmoReadingList, '/atmo', endpoint='atmo')
api.add_resource(AtmoReading, '/atmo/<datetime>')
