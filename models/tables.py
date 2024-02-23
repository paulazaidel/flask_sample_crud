from sqlalchemy import Table, Column, ForeignKey

from extensions import Base

game_console_association_table = Table(
    "game_console_association",
    Base.metadata,
    Column("game_id", ForeignKey("games.id"), primary_key=True),
    Column("console_id", ForeignKey("consoles.id"), primary_key=True),
)
