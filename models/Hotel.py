from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=2))
    preco = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(50))


    def __init__(self, hotel_id, nome, estrelas, preco, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.preco = preco
        self.cidade = cidade

    def transform_json(self):
        return{
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'preco': self.preco,
            'cidade': self.cidade
        }
    
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None
    
    def save_register(self):
        banco.session.add(self)
        banco.session.commit()
    
