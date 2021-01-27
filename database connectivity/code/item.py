import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    @jwt_required()  #only get will require authorization
    def get(self, name):  # flask restful method accessed using get
        # print(items)
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item}, 200 if item else 400
        item = self.find_by_name(name)

        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        # if next(filter(lambda x: x['name'] == name, items), None):
        #     return {'message': "An item with name '{}' already exists".format(name)}, 400
        if self.find_by_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        # items.append(item)
        try:
            self.insert(item)
        except:
            return {"message": "An error occured while inserting"}, 500 #Internal Server Error

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

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
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            # item = {'name': name, 'price': data['price']}
            # items.append(item)
            try:
                self.insert(updated_item)
            except:
                return {"message", "An error occured while inserting"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occured while updating"}, 500
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()


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
        return  {'items': items}