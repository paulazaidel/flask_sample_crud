from app import marshmallow
from models import Category


class CategorySchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
