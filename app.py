from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy import create_engine

from apis.category_api import ns as ns_category
from apis.game_api import ns_games
from auth.routes import blueprint as auth_bp
from config import DEBUG, SECRET_KEY
from extensions import db, api, SQLALCHEMY_DATABASE_URI, Base, db_session
from game.routes import blueprint as game_bp
from log import logger


app = Flask(__name__)
migrate = Migrate(app, db)

app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gameLibrary.db"


# SQLAlchemy
db.init_app(app)
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)

# Api
api.init_app(app)
api.add_namespace(ns_games)
api.add_namespace(ns_category)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    logger.info("Starting Application")
    Base.metadata.create_all(bind=engine)

    app.run(port=8080, debug=DEBUG)
