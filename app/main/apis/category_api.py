from flask import jsonify
from flask_restx import Resource, fields
from app.main.extensions import api, db_session
from app.main.models import Category
from app.main.models import CategorySchema

ns = api.namespace("CATEGORIES", path="categories")


category_serializer = ns.model(
    "Category",
    {
        "id": fields.Integer(readonly=True),
        "name": fields.String(size=50, required=True),
        "description": fields.String(size=100),
    },
)

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@ns.route("/")
class CategoryAPI(Resource):
    @ns.response(200, "List all categories", [category_serializer])
    @api.marshal_list_with(category_serializer)
    def get(self):
        categories = Category.query.all()
        return categories_schema.dump(categories)

    @api.expect(category_serializer)
    @api.marshal_with(category_serializer, code=201)
    def post(self):
        category = Category("teste", "teste")
        db_session.add(category)
        db_session.commit()
        return jsonify(data="Add")


@ns.route("/<int:id>")
class CategoryItemAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
