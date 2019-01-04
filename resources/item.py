from models.item import ItemModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('price', 
    type=float,
    required=True, 
    help="This field cannot be blank")
  parser.add_argument('store_id', 
    type=int,
    required=True, 
    help="Every item needs a store id")

  @jwt_required()
  def get(self, name):
    item = ItemModel.find_by_name(name)
    if item:
      return item.json()
    return {'message': 'item not found'}, 404
  
  @jwt_required()
  def post(self, name):
    if ItemModel.find_by_name(name):
      return {'message': 'this item already exists'}

    data = Item.parser.parse_args()
    item = ItemModel(name, **data)
    try:
      item.save()
      return item.json(), 201
    except:
      return {'message': 'An error occured saving item to database'}, 500
  
  @jwt_required()
  def delete(self, name):
    item = ItemModel.find_by_name(name)
    if item:
      #try:
      item.delete()
      #except:
        #return {'message': 'An error occured while deleting object from datebase'}, 500
    return {'message': 'item deleted'}
    
  
  @jwt_required()
  def put(self, name):
    data = Item.parser.parse_args()
    item = ItemModel.find_by_name(name)
    if item:
      item.price = data['price']
      item.store_id = data['store_id'] 
    else:
      item = ItemModel(name, **data)
    
    item.save()
    return item.json()


class Items(Resource):
  def get(self):
    return {'items': [item.json() for item in ItemModel.query.all()]}