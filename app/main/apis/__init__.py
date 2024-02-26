from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Game Library",
    version="1.0",
    description="API Doc",
    # doc="/swagger",
    prefix="/api/v1",
)


# api.add_namespace(ns_games)
# api.add_namespace(ns_category)
