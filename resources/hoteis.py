from flask_restful import Resource, reqparse
from models.Hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return({'Hoteis':[hotel.transform_json() for hotel in HotelModel.query.all()]})


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('preco')
    argumentos.add_argument('cidade')

    def get(self,hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            return hotel.transform_json()
        return {'message':'Hotel not found'}, 404
    
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
        
            

