from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

api = Api(
    version="1.0",
    title="Game Library",
    description="API Doc",
    doc="/swagger",
    prefix="/api/v1",
)
