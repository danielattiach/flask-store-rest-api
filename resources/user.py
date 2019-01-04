from models.user import UserModel
from flask_restful import Resource, reqparse
from app import bcrypt

class UserRegister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
    'username',
    type=str,
    required=True,
    help="This field cannot be blank"
  )
  parser.add_argument(
    'password',
    type=str,
    required=True,
    help="This field cannot be blank"
  )

  @classmethod
  def post(cls):
    data = cls.parser.parse_args()
    
    if UserModel.find_by_username(data['username']):
      return { 'message': 'this username is already taken' }
    
    pw_hash = bcrypt.generate_password_hash(data['password'], 10)

    new_user = UserModel(data['username'], pw_hash)
    new_user.save()

    return { 'message': 'User created successfully' }, 201