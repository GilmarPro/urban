from flask.views import MethodView
from flask import request
from models.Teams import Teams
from models.Players import Players
from app import db        

class TeamAPI(MethodView):
    def post(self):
        player_id = request.form.get('player_id', '')
        team_id = request.form.get('team_id', '')
        if player_id != '' and team_id != '':
            player = Players.query.filter_by(id=player_id).first()

            team = Teams.query.filter_by(id=team_id).first()

            if len(team.players) >= 5:
                return 'The team is full'

            team.players.append(player)

            db.session.commit()
            return 'OK'
        
        return 'Nao entrou no if'

    def get(self):
        team_id = request.args.get('team_id', '')

        if team_id != '':
            return {'Players': [p.toJSON() for p in Teams.query.filter_by(id=team_id).one().players]}

    def delete(self):
        player_id = request.form.get('player_id', '')
        team_id = request.form.get('team_id', '')
        if player_id != '' and team_id != '':
            player = Players.query.filter_by(id=player_id).first()

            team = Teams.query.filter_by(id=team_id).first()
            team.players.remove(player)

            db.session.commit()
            return 'OK'
        
        return 'Nao entrou no if'