from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'users'

    user_id = banco.Column(banco.Integer, primary_key=True)
    user = banco.Column(banco.String(10))
    senha = banco.Column(banco.String())

    def __init__(self, user, senha):
        self.user = user
        self.senha = senha

    def transform_json(self):
        return{
            'user_id': self.user_id,
            'user': self.user
        }
    
    @classmethod
    def find_user(cls, user):
        user = cls.query.filter_by(user=user).first()
        if user:
            return user
        return None
    
    def save_register(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_register(self):
        banco.session.delete(self)
        banco.session.commit()
    