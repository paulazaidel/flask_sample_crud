from flask import Flask

from auth.routes import blueprint as auth_bp
from game.routes import blueprint as game_bp
from config import SECRET_KEY, DEBUG


def create_app():
    flask = Flask(__name__)
    flask.secret_key = SECRET_KEY

    return flask


app = create_app()
app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)


if __name__ == '__main__':
    app.run(port=8080, debug=DEBUG)
