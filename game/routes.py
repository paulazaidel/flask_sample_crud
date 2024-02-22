from flask import Blueprint

from game.controller import index, new, create

blueprint = Blueprint("game", __name__)

blueprint.route("/", methods=["GET"])(index)
blueprint.route("/new", methods=["GET"])(new)
blueprint.route("/create", methods=["POST"])(create)
