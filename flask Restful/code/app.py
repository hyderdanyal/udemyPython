from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "BenandJerry" #supposed to be secret and not published in the code but secured
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth endpoint created automatically

items = []

class Item(Resource):
    @jwt_required()  #only get will require authorization
    def get(self, name):  # flask restful method accessed using get
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 400

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                             type=float,
                             required=True,
                             help="this field cannot be blank"
                             )
        data = parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class Items(Resource):
    def get(self):
        return items, 200


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
