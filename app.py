from flask import Flask

from apis.game_api import ns_games
from auth.routes import blueprint as auth_bp
from extensions import db, api
from game.routes import blueprint as game_bp
from config import SECRET_KEY, DEBUG

app = Flask(__name__)


def initialize_app(app):
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///gameLibrary.db'

    # SQLAlchemy
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    # Api
    api.init_app(app)
    api.add_namespace(ns_games)


if __name__ == '__main__':
    initialize_app(app)
    app.run(port=8080, debug=DEBUG)
