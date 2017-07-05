from admrsh import db


class AtmoReading(db.Model):
    """."""
    temp = db.Column(db.Float)
    humd = db.Column(db.Float)
    datetime = db.Column(db.DateTime)

    def __init__(self, temp, humd, datetime):
        self.temp = temp
        self.humd = humd
        self.datetime = datetime

    def __repr__(self):
        return '<AtmoReading {}>'.format(self.datetime.isoformat(' '))
