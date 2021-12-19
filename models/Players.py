from app import db

class Players(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)

    def toJSON(self):
        return {'id': self.id, 'name': self.name, 'mail': self.mail}

    def __repr__(self):
        return '<Player %r>' % self.id