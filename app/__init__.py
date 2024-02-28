import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.database import init_sqlalchemybase
from app.main import register_blueprints, register_namespaces
from app.main.apis import api
from config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    config_name = os.getenv("ENVIRONMENT") or "development"

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)
    register_namespaces(api)

    init_sqlalchemybase()

    return app
