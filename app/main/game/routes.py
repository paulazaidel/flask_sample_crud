from flask import Blueprint

from game.controller import create, index, new

blueprint = Blueprint("game", __name__)

blueprint.route("/", methods=["GET"])(index)
blueprint.route("/new", methods=["GET"])(new)
blueprint.route("/create", methods=["POST"])(create)
