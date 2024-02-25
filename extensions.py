from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///gameLibrary.db"


Base = declarative_base()
db = SQLAlchemy(model_class=Base)

api = Api(
    version="1.0",
    title="Game Library",
    description="API Doc",
    doc="/swagger",
    prefix="/api/v1",
)
Base.query = db_session.query_property()
