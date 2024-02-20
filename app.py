from flask import Flask

from auth.routes import blueprint as auth_bp
from game.routes import blueprint as game_bp
from config import SECRET_KEY, DEBUG, db

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///gameLibrary.db'

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8080, debug=DEBUG)
