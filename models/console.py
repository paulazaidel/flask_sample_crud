from typing import List, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from extensions import Base, db
from models.tables import game_console_association_table


class Console(Base):
    __tablename__ = "consoles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    games: Mapped[List["Console"]] = relationship(
        secondary=game_console_association_table, back_populates="consoles"
    )
