import time

from flask_restful import Resource, reqparse

from admrsh import api
from .models import AtmoReading


query_parser = reqparse.RequestParser()
query_parser.add_argument('startAt', location='args')
query_parser.add_argument('endAt', location='args')


class AtmoReadings(Resource):
    def get(self):
        args = query_parser.parse_args()
        start = args.pop('startAt', None)
        end = args.pop('endAt', None)
        if valid_date(start):
            if valid_date(end):
                # from start to end
                pass
            else:
                # find one
                pass
        return [a.as_dict() for a in AtmoReading.query.all()]


def valid_date(date_str):
    # 404 abort instead of display all?
    try:
        time.strptime(date_str, '%Y-%m-%d')
        return True
    except (ValueError, TypeError):
        return False
# END valid_date()



api.add_resource(AtmoReadings, '/atmo', endpoint='atmo')
