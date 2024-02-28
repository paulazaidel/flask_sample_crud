from auth.controller import authenticate, login, logout
from flask import Blueprint

blueprint = Blueprint("auth", __name__)

blueprint.route("/login", methods=["GET"])(login)
blueprint.route("/authenticate", methods=["POST"])(authenticate)
blueprint.route("/logout", methods=["GET"])(logout)
