from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from models import *

def index():
    return '<h1> OK </h1>'
app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
    from views import *
    app.add_url_rule('/players/', view_func=PlayerAPI.as_view('players_api'))
    app.add_url_rule('/matches/', view_func=MatchAPI.as_view('matches_api'))
    app.add_url_rule('/teams/', view_func=TeamAPI.as_view('matches_man_api'))
    app.run()