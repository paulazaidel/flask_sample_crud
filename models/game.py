from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from extensions import Base
from models.console import Console
from models.tables import game_console_association_table


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="games")

    consoles: Mapped[List["Console"]] = relationship(
        secondary=game_console_association_table, back_populates="games"
    )

    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console
