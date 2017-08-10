from admrsh import db


class AtmoRead(db.Model):
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
