from app import db

teams_has_players = db.Table('teams_has_players', db.Model.metadata,
    db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True),
    db.Column('player_id', db.Integer, db.ForeignKey('players.id'), primary_key=True)
)

class Teams(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship('Players', secondary=teams_has_players)

    def __repr__(self):
        return '<Team %r>' % self.id