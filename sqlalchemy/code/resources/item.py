import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    @jwt_required()  #only get will require authorization
    def get(self, name):  # flask restful method accessed using get

        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'Item not found'}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 400
        data = request.get_json()
        item = ItemModel(name, **data)
        try:

            item.save_to_db()
        except:
             return {"message": "An error occured while inserting"}, 500 #Internal Server Error

        return item.json()
        # return item.json(), 201


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 404


    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                             type=float,
                             required=True,
                             help="this field cannot be blank"
                             )
        data = parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'])
        item.save_to_db()

        return item.json()


class Items(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'id': row[0], 'name': row[1], 'price': row[2]})

        connection.close()
        return {'items': items}

