from flask_restful import Resource, reqparse
from models.Hotel import HotelModel


hoteis = [
    {
        'hotel_id':'bravo',
        'estrelas':'4',
        'preco':'200.00'
    },
    {
        'hotel_id':'charlie',
        'estrelas':'3',
        'preco':'100.00'
    },
    {
        'hotel_id':'alpha',
        'estrelas':'5',
        'preco':'400.00'
    }
]

class Hoteis(Resource):
    def get(self):
        return({'Hoteis':hoteis})


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('preco')
    argumentos.add_argument('cidade')

    def get(self,hotel_id):
        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            return hotel
        return {'message':'Hotel não ecnontrado'}, 404
    
    def post(self,hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message":"Hotel '{}' is alredy registered".format(hotel_id)}

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_register()
        return hotel.transform_json()

    def put(self,hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.transforma_json()

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel
        
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]

        return {'message':'Hotel Deletado'}
        
            

