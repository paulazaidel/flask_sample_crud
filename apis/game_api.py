from flask_restx import Resource, fields, Namespace

api = Namespace('categories', description='Operations related to categories')

game_serializer = api.model('Game', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(size=50, required=True, description='The game name'),
    'category': fields.String(size=40, required=True, description='The game category'),
    'console': fields.String(size=20, required=True, description='The console name'),
})


@api.route('/')
class GameApi(Resource):
    @api.marshal_list_with(game_serializer)
    def get(self):
        return NotImplemented

    @api.expect(game_serializer)
    @api.marshal_with(game_serializer, code=201)
    def post(self):
        return NotImplemented


@api.route('/<int:id>')
@api.response(404, 'Not found.')
class GameItemApi(Resource):
    @api.marshal_with(game_serializer)
    def get(self, id):
        return NotImplemented
