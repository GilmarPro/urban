from flask.views import MethodView
from flask import make_response, jsonify, request
from datetime import datetime
from models.Teams import Teams
from models.Players import Players
from models.Matches import Matches
from app import db

class MatchAPI(MethodView):
    def get(self):
        data = request.args.get('id', '')

        if data != '':
            match = Matches.query.filter_by(id=data).first()
            return {match.id : {'address': match.address, 'day': match.day.strftime('%d-%m-%Y'), 'hour': match.hour.strftime('%H:%M')}}
        
        matches = Matches.query.all()
        return {match.id : {'address': match.address, 'day': match.day.strftime('%d-%m-%Y'), 'hour': match.hour.strftime('%H:%M')} for match in matches}

    def post(self):
        address = request.form.get('address', '')
        day = request.form.get('day', '')
        hour = request.form.get('hour', '')
        if address != '' and day != '' and hour != '':
            day = datetime.strptime(day, '%d-%m-%Y').date()
            hour = datetime.strptime(hour, '%H:%M').time()

            new_match = Matches(address=address, day=day, hour=hour, team_A=Teams(), team_B=Teams())
            db.session.add(new_match)
            db.session.commit()
            return f'Match added'

        return 'Address, day and hour have to be set'

    def delete(self):
        id = request.args.get('id', '')
        match = None

        if id != '':
            match = Matches.query.filter_by(id=id).first()
            if match != None:
                db.session.delete(match)
                db.session.commit()

        if match != None:
            return f'match {id} deleted'

        return f'No match was deleted'

    def put(self):
        id = request.form.get('id', '')

        if id != '':
            match = Matches.query.filter_by(id=id).first()
        else:
            return 'Inform a valid match id'

        if match:
            address = request.form.get('address', match.address)
            day = request.form.get('day', match.day)
            hour = request.form.get('hour', match.hour)

            if type(day) == str:
                day = datetime.strptime(day, '%d-%m-%Y').date()
            if type(hour) == str:
                hour = datetime.strptime(hour, '%H:%M').time()
        else:
            return "There's no match with specified id"

        if id != '':
            match = Matches.query.filter_by(id=id).first()
        
            match.address = address
            match.day = day
            match.hour = hour
            
            db.session.commit()

            return f'match {id} modified'        

class TeamAPI(MethodView):
    def post(self):
        player_id = request.form.get('player_id', '')
        team_id = request.form.get('team_id', '')
        if player_id != '' and team_id != '':
            player = Players.query.filter_by(id=player_id).first()

            team = Teams.query.filter_by(id=team_id).first()
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