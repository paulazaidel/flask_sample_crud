from sqlalchemy import String


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(primary_key=True, autoincrement=True)
    name = db.Column(String(50), unique=True, nullable=False)
    description = db.Column(String(100), nullable=True)

    # games: Mapped[List["Game"]] = relationship("Game", back_populates="category")

    def __init__(self, name, description: None):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Category '{}'>".format(self.name)
