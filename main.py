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
    response = []

    for index in data['origin']:
        if data[request_type][index] == request or data[request_type + '_full_name'][index] == request:
            response.append({
                'origin': data['origin'][index],
                'destination': data['destination'][index]
            })

    print(data['origin_full_name'][3].upper())

    response = json.dumps(response, indent = 3)

    return response


@app.get('/autosuggest')
def autosuggest():
    data = pd.read_csv(data_path)
    data = data.to_dict()

    response = []

    for index in data['origin']:
        response.append(str(data['origin'][index]))
        response.append(str(data['origin_full_name'][index]))
        response.append(str(data['destination'][index]))
        response.append(str(data['destination_full_name'][index]))

    response = [*set(response)]
    response.sort(key=lambda x : len(x))
    response = json.dumps(response, indent = 0)

    return response

