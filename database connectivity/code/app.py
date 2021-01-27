from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Items,Item

app = Flask(__name__)
app.secret_key = "BenandJerry" #supposed to be secret and not published in the code but secured
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth endpoint created automatically

# items = []
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
