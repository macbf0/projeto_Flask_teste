class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, preco, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.preco = preco
        self.cidade = cidade

    def transforma_json(self):
        return{
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'preco': self.preco,
            'cidade': self.cidade
        }