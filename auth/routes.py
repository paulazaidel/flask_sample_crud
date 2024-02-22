from flask import Blueprint

from auth.controller import login, authenticate, logout

blueprint = Blueprint("auth", __name__)

blueprint.route("/login", methods=["GET"])(login)
blueprint.route("/authenticate", methods=["POST"])(authenticate)
blueprint.route("/logout", methods=["GET"])(logout)
