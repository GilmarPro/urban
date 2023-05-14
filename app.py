from flask import Flask
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    from views.player import PlayerAPI
    from views.team import TeamAPI
    from views.match import MatchAPI

    app.add_url_rule('/players/', view_func=PlayerAPI.as_view('players_api'))
    app.add_url_rule('/matches/', view_func=MatchAPI.as_view('matches_api'))
    app.add_url_rule('/teams/', view_func=TeamAPI.as_view('matches_man_api'))
    app.run()
