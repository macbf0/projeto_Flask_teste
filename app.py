from flask import Flask
from flask_restful import Api
from resources.hoteis import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis,'/hoteis')
api.add_resource(Hotel, '/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)