from flask import Flask, request
from flask_restful import Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store,StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' # indicate the type and address of the database
app.config['SQLALCHEMY_TRACK_MODIFICATIOaNS'] = False # SQLALCHEMY has a better tracking
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf equals to @app.route('...')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
