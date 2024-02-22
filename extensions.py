from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

api = Api(
    version="1.0",
    title="Game Library",
    description="API Doc",
    doc="/swagger",
    prefix="/api/v1",
)
