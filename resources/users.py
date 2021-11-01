from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    def get(self, user):
        user = UserModel.find_user(user)
        if user:
            return user.transform_json()
        return {'message':'User not found'}, 404

    def delete(self, user):
        user_delete = UserModel.find_user(user)
        if user_delete:
            user_delete.delete_register()
            return {'message':'User deleted'}
        return {'message':'User not found'}, 404

class UserRegister(Resource):

    def post(self):
        arguments = reqparse.RequestParser()
        arguments.add_argument('user')
        arguments.add_argument('senha')
        dados = arguments.parse_args()
        user_find = UserModel.find_user(dados['user'])
        if user_find:
            return {'message':'User has already been registered'}
        
        user = UserModel(**dados)
        user.save_register()
        return user.transform_json()
        