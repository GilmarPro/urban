from flask.views import MethodView
from flask import make_response, request

from models.Players import add_player, show_player, del_player, up_player

class PlayerAPI(MethodView):
    def get(self):
        data = request.args.get('id', '')
        if data != '':
            player = show_player(data)
            return f'Player {player.name}'
        
        players = show_player()
        return {player.id : player.name for player in players}

    def post(self):
        data = request.form.get('name', '')
        if data != '':
            add_player(data)
            print(data)
            return f'Player {data} added'

        return 'Name has to be set'

    def delete(self):
        data = request.args.get('id', '')
        player = None

        if data != '':
            player = del_player(data)

        if player != None:
            return f'Player {data} deleted'

        return f'No Player was deleted'

    def put(self):
        id = request.form.get('id', '')
        name = request.form.get('name', '')
        if id != '' and name != '':
            up_player(id, name)
            return f'Player {id} modified'

        return 'Name and id should be informed'      