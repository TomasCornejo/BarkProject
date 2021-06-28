from app import db


class DataRow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetimeRegister = db.Column(db.String(20), index=True, unique=True)
    value: int = db.Column(db.Integer)

    def __repr__(self):
        return '<{dTime}: {value}>'.format(dTime=self.datetimeRegister, value=self.value)
