from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta
from resources.item import Item, Items
from resources.store import Store, Stores 

app = Flask(__name__)
app.secret_key = 'dingaling'
bcrypt = Bcrypt(app)
api = Api(app)

"""
JWT creates a new endpoint, '/auth'
when we call it, we send it a username and password
those are sent to the 'authenticate' function for verification
if verified, the 'authenticate' function returns the user, 
which becomes the identity.
Next, the '/auth' endpoint returns a token
Then JWT calls the identity and passes it the token.
identity then uses the token to find the user and returns it

"""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=86400)

@app.before_first_request
def create_tables():
  db.create_all()

if __name__ == '__main__':
  from db import db
  from security import authenticate, identity
  from resources.user import UserRegister

  api.add_resource(Item, '/items/<string:name>')
  api.add_resource(Items, '/items')
  api.add_resource(Store, '/stores/<string:name>')
  api.add_resource(Stores, '/stores')
  api.add_resource(UserRegister, '/register')
  jwt = JWT(app, authenticate, identity)
  db.init_app(app)
  app.run(port=5000, debug=True)