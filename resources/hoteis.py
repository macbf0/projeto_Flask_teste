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
        finded_hotel = HotelModel.find_hotel(hotel_id)
        if finded_hotel:
            finded_hotel.update_hotel(**dados)
            finded_hotel.save_register()
            return finded_hotel.transform_json()
        new_hotel = HotelModel(hotel_id, **dados)
        new_hotel.save_register()
        return new_hotel.transform_json()
    
    def delete(self, hotel_id):
        delete_hotel = HotelModel.find_hotel(hotel_id)
        if delete_hotel:
            delete_hotel.delete_register()
            return {'message':'Hotel Deleted'}
        return {'message':'Hotel not found'}
        
            

