from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_path = './data/flights.csv'


@app.get('/request')
def request(request, request_type):
    data = pd.read_csv(data_path)
    data = data.to_dict()
    response = {
        'origin': [],
        'destination': []
    }

    for index in data['origin']:
        if data[request_type][index] == request or data[request_type + '_full_name'] == request:
            response['origin'].append(data['origin'][index])
            response['destination'].append(data['destination'][index])

    # if request_type == 'destination':
    #     response = dict(reversed(response.items()))

    response = json.dumps(response, indent = 3)

    return response


@app.get('/autosuggest')
def autosuggest():
    data = pd.read_csv(data_path)
    data = data.to_dict()

    response = [{
    'origin': [],
    'origin_full_name': [],
    'destination': [],
    'destination_full_name': []
    }]

    for index in data['origin']:
        response[0]['origin'].append(data['origin'][index])
        response[0]['origin_full_name'].append(data['origin_full_name'][index])
        response[0]['destination'].append(data['destination'][index])
        response[0]['destination_full_name'].append(data['destination_full_name'][index])    

    response = json.dumps(response, indent = 4)

    return response
