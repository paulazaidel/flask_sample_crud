from flask import Blueprint
from flask_restx import Api
from apis.game_api import api as category_api

api_bp = Blueprint('api', __name__, url_prefix='/api')

api_v1 = Api(
    version='1.0',
    title='Game Library',
    description='API Doc',
    doc='/swagger',
    blueprint=api_bp
)


def config_api_v1(app):
    api_v1.init_app(app=app)

    api_v1.add_namespace(category_api)


