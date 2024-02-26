# from typing import List
#
# from sqlalchemy import ForeignKey, String
# from sqlalchemy.orm import Mapped, mapped_column, relationship
#
# from app.main.extensions import Base
# from app.main.models.tables import game_console_association_table
#
#
# class Game(Base):
#     __tablename__ = "games"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
#
#     category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
#     category: Mapped["Category"] = relationship("Category", back_populates="games")
#
#     consoles: Mapped[List["Console"]] = relationship(
#         secondary=game_console_association_table, back_populates="games"
#     )
