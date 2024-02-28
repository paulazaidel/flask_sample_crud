from flask import jsonify, request
from flask_restx import Resource, fields

from app.database import db_session
from app.main.apis import api
from app.main.models import Category, CategorySchema

ns = api.namespace("CATEGORIES", path="/categories")


model = ns.model(
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
    @ns.response(200, "List all categories", [model])
    @api.marshal_list_with(model)
    def get(self):
        categories = Category.query.all()
        return categories_schema.dump(categories)

    @api.expect(model)
    @api.marshal_with(model, code=201)
    def post(self):
        request_json = request.get_json()

        name = request_json["name"]

        data = categories_schema.load(request_json)
        db_session.add(data)
        db_session.commit()
        return jsonify(data="Added"), 201


@ns.route("/<int:id>")
class CategoryItemAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
