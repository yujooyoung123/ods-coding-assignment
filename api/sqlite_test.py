import sqlite3 as sq
import pandas as pd
from fastapi import FastAPI
import sqlalchemy

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

def query_data(query):
    response = []

    for 

# query specific column

request = sqlalchemy.select([flight_table]).where(
    flight_table.columns.origin_full_name == 'Nashville Intl')

result_proxy = conn.execute(request)

result = result_proxy.fetchall()

print(result)
