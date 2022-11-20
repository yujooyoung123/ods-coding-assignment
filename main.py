from fastapi import FastAPI
import pandas as pd

app = FastAPI()

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

    if request_type == 'destination':
        response = dict(reversed(response.items()))

    return response


@app.get('/autosuggest')
def autosuggest():
    data = pd.read_csv(data_path)
    data = data.to_dict()

    return data
