import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    @jwt_required()  #only get will require authorization
    def get(self, name):  # flask restful method accessed using get
        # print(items)
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item}, 200 if item else 400
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'Item not found'}, 404


    def post(self, name):
        # if next(filter(lambda x: x['name'] == name, items), None):
        #     return {'message': "An item with name '{}' already exists".format(name)}, 400
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 400
        data = request.get_json()
        # item = {'name': name, 'price': data['price']}
        item = ItemModel(name, data['price'])
        # items.append(item)
        try:
            item.insert()
        except:
            return {"message": "An error occured while inserting"}, 500 #Internal Server Error

        return item.json(), 201


    def delete(self, name):
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                             type=float,
                             required=True,
                             help="this field cannot be blank"
                             )
        data = parser.parse_args()
        # item = next(filter(lambda x: x['name'] == name, items), None)
        item = ItemModel.find_by_name(name)
        # updated_item = {'name': name, 'price': data['price']}
        updated_item = ItemModel(name, data['price'])
        if item is None:
            # item = {'name': name, 'price': data['price']}
            # items.append(item)
            try:
                updated_item.insert()
            except:
                return {"message", "An error occured while inserting"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error occured while updating"}, 500
        return updated_item.json()


class Items(Resource):
    def get(self):
        # return items, 200
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name':row[0], 'price': row[1]})

        connection.close()
        return {'items': items}

