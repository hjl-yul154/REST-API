import os

from flask import Flask, request
from flask_restful import Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
uri = os.getenv("DATABASE_URL",'sqlite:///data.db')
if uri.startswith("postgres://"): # change the beginning potion *version error
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri # indicate the address of DB
app.config['SQLALCHEMY_TRACK_MODIFICATIOaNS'] = False  # SQLALCHEMY has a better tracking
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf equals to @app.route('...')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
