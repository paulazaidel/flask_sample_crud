from sqlalchemy import Column, ForeignKey, Table

from app.main.extensions import Base

game_console_association_table = Table(
    "game_console_association",
    Base.metadata,
    Column("game_id", ForeignKey("games.id"), primary_key=True),
    Column("console_id", ForeignKey("consoles.id"), primary_key=True),
)
