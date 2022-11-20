from flask import Flask
from flask_restful import Resource, Api
import pandas as pd
from marshmallow import Schema, fields

class flight_request_schema(Schema):
    request_station = fields.String()
    request_name = fields.String()

app = Flask(__name__)
api = Api(app)
schema = flight_request_schema()

data_path = './data/flights.csv'


class OriginAPI(Resource):
    def get(self, request):
        data = pd.read_csv(data_path)
        data = data.to_dict()
        response = {
            'origin': [],
            'destination': []
        }
        for index in data['origin']:
            if data['origin'][index] == request or data['origin_full_name'] == request:
                response['origin'].append(data['origin'][index])
                response['destination'].append(data['destination'][index])

        return response


class DestinationAPI(Resource):
    def get(self, request):
        data = pd.read_csv(data_path)
        data = data.to_dict()
        response = {
            'destination': [],
            'origin': []
        }
        for index in data['destination']:
            if data['destination'][index] == request or data['destination_full_name'] == request:
                response['destination'].append(data['destination'][index])
                response['origin'].append(data['origin'][index])

        return response

api.add_resource(OriginAPI, '/origin')
api.add_resource(DestinationAPI, '/destination')


if __name__ == "__main__":
    app.run()
