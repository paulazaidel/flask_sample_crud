from typing import Optional

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import SQLAlchemyBase, db_session


class Category(SQLAlchemyBase):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # games: Mapped[List["Game"]] = relationship("Game", back_populates="category")

    def __init__(self, name: str, description: None):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Category '{}'>".format(self.name)


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        sqla_session = db_session
