import sqlite3 as sq
import pandas as pd
from fastapi import FastAPI
import sqlalchemy
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_path = './data/flights.db'

# conn = sq.connect('data/flights.db')

# cur = conn.cursor()

# for row in cur.execute('SELECT origin FROM flights'):
#     if row == 'BNA':
#         print(row)

# conn.close()

engine = sqlalchemy.create_engine("sqlite:///./data/flights.db")
conn = engine.connect()
metadata = sqlalchemy.MetaData()
flight_table = sqlalchemy.Table('flights', metadata, autoload=True, autoload_with=engine)

# print column titles
# print(flight_table.columns.keys())

@app.get('/query')
def query_data(query, query_type):

    if len(query) > 3:
        query_type = query_type + '_full_name'

    request = sqlalchemy.select([flight_table.columns.origin, flight_table.columns.destination]).where(
        flight_table.columns[query_type] == query
    )

    result_proxy = conn.execute(request)
    result = result_proxy.fetchall()

    return result

# query specific column

name = 'origin'
station = 'Nashville Intl'

# request = sqlalchemy.select([flight_table.columns.origin, flight_table.columns.destination]).where(
#     flight_table.columns.origin_full_name == 'Nashville Intl')

# result_proxy = conn.execute(request)

# result = result_proxy.fetchall()

# print(result)

request = sqlalchemy.select([flight_table.columns.origin, flight_table.columns.destination]).where(
    flight_table.columns[name + '_full_name'] == station)

result_proxy = conn.execute(request)

result = result_proxy.fetchall()

print(result)