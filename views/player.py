from flask.views import MethodView
from flask import make_response, request
from app import db
from models.Players import Players

class PlayerAPI(MethodView):
    def get(self):
        data = request.args.get('id', '')

        if data != '':
            player = Players.query.filter_by(id=data).first()
            if player:
                return f'Player {player.name}'
            return 'No player found'
        
        players = Players.query.all()
        return {player.id : {'name': player.name, 'mail': player.mail} for player in players}

    def post(self):
        name = request.form.get('name', '')
        mail = request.form.get('mail', '')
        if (name != '') and (mail != ''):
            db.session.add(Players(name=name, mail=mail))
            db.session.commit()
            return f'Player {name} added'

        return 'Name and mail have to be set'

    def delete(self):
        data = request.args.get('id', '')
        player = None

        if data != '':  
            player = Players.query.filter_by(id=data).first()
            if player != None:
                db.session.delete(player)
                db.session.commit()

        if player != None:
            return f'Player {data} deleted'

        return f'No Player was deleted'

    def put(self):
        id = request.form.get('id', '')
        name = request.form.get('name', '')
        mail = request.form.get('mail', '')
        if (id != '') and (name != '') and (mail != ''):
            player = Players.query.filter_by(id=id).first()
            if player:
                player.name = name
                player.mail = mail
                db.session.commit()
            return f'Player {id} modified'

        return 'Name and id should be informed'      