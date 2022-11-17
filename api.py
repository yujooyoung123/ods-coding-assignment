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
    def get(self):
        data = pd.read_csv(data_path)
        data = data.to_dict()
        response = {
            'origin': [],
            'destination': []
        }
        for index in data['origin']:
            if data['origin'][index] == 'BNA' or data['origin_full_name'] == 'Nashville':
                response['origin'].append(data['origin'][index])
                response['destination'].append(data['destination'][index])

        return response


api.add_resource(OriginAPI, '/origin')

if __name__ == "__main__":
    app.run()