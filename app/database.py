import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from config import config

config_name = os.getenv("ENVIRONMENT") or "development"
engine = create_engine(config[config_name].SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
SQLAlchemyBase = declarative_base()
SQLAlchemyBase.query = db_session.query_property()


def init_sqlalchemybase():
    SQLAlchemyBase.metadata.create_all(bind=engine)
