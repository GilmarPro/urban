from app import db

class Players(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Player %r>' % self.id

def add_player(name):
    db.session.add(Players(name=name))
    db.session.commit()

def show_player(id=None):
    if id:
        return Players.query.filter_by(id=id).first()

    return Players.query.all()

def del_player(id):
    player = Players.query.filter_by(id=id).first()
    if player != None:
        db.session.delete(player)
        db.session.commit()
        
    return player

def up_player(id, name):
    player = Players.query.filter_by(id=id).first()
    player.name = name
    db.session.commit()