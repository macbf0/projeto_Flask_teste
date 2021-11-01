from flask_restful import Resources
from models.user import UserModel

class User(Resources):
    def get(self, user):
        user = UserModel.find_user(user)
        if user:
            return user.transform_json()
        return {'message':'User not found'}

    def delete(self, user):
        user_delete = UserModel.find_user(user)
        if user_delete:
            try:
                user_delete.delete_register(self)
            except:
                return {'message':'Aplication could not delete'}
            return {'message':'User deleted'}
        return {'message':'User not found'}
        