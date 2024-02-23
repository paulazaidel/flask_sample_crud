from typing import List, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from extensions import Base, db


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    games: Mapped[List["Game"]] = relationship(back_populates="category")

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
