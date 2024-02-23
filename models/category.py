from typing import Optional, List

from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from extensions import db, Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    games: Mapped[List["Game"]] = relationship(back_populates="category")

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
