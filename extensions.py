from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from app import engine

SQLALCHEMY_DATABASE_URI = "sqlite:///gameLibrary.db"


Base = declarative_base()
db = SQLAlchemy(model_class=Base)

metadata = MetaData()


api = Api(
    version="1.0",
    title="Game Library",
    description="API Doc",
    doc="/swagger",
    prefix="/api/v1",
)
