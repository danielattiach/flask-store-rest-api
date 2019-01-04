from flask_restful import Resource
from models.store import StoreModel
from flask_jwt import jwt_required

class Store(Resource):
  
  def get(self, name):
    store = StoreModel.find_by_name(name)
    if store:
      return store.json()
    return {'message': 'store not found'}, 404
  
  @jwt_required()
  def post(self, name):
    if StoreModel.find_by_name(name):
      return {'message': f"a store with name '{name}' already exists"}, 400
    store = StoreModel(name)
    try:
      store.save()
      return store.json(), 201
    except:
      return {'message': 'an error occured while trying to save the store'}, 500
  
  @jwt_required()
  def delete(self,  name):
    store = StoreModel.find_by_name(name)
    if store:
      store.delete()
    return {'message': 'the store was successfully deleted'}

class Stores(Resource):
  def get(self):
    return {'stores': [store.json() for store in StoreModel.query.all()]}