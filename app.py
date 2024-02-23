from flask import Flask
from flask_migrate import Migrate

from apis.game_api import ns_games
from auth.routes import blueprint as auth_bp
from config import DEBUG, SECRET_KEY
from extensions import db, api
from game.routes import blueprint as game_bp
from log import logger


app = Flask(__name__)
migrate = Migrate(app, db)

app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gameLibrary.db"


# SQLAlchemy
db.init_app(app)

# Blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)

# Api
api.init_app(app)
api.add_namespace(ns_games)


if __name__ == "__main__":
    logger.info("Starting Application")
    app.run(port=8080, debug=DEBUG)
