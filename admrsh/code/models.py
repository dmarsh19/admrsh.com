from flask import jsonify
from flask_restful import Resource

from admrsh import db


class AtmoReading(db.Model):
    """."""
    __tablename__ = 'DHT'
    id = db.Column('oid', db.Integer, primary_key=True)
    temp = db.Column(db.Float)
    humd = db.Column(db.Float)
    datetime = db.Column(db.Text)

    def __init__(self, temp, humd, datetime):
        self.temp = temp
        self.humd = humd
        self.datetime = datetime

    def as_dict(self):
        """return results as a dict with key equal to field name."""
        d = {}
        for c in self.__table__.columns:
            if c.name != 'oid':
                d[c.name] = getattr(self, c.name)
        return d


class AtmoReadings(Resource):
    def get(self):
        return jsonify([a.as_dict() for a in AtmoReading.query.all()])
