from models import db


class Matches(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    day = db.Column(db.Date, nullable=False)
    hour = db.Column(db.Time, nullable=False)
    team_A_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team_B_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team_A = db.relationship('Teams', foreign_keys=[team_A_id])
    team_B = db.relationship('Teams', foreign_keys=[team_B_id])

    def __repr__(self):
        return '<Match %r>' % self.id