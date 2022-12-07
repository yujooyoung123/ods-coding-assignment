# ODS Full Stack Coding Assignment

## Assignment

Create a web application that allows a user to search for flights and display the results in a tabular view.

## Features

1. Allow the user to enter a station (destination or origin) to search flights. Display the results in a table.

2. Provide an auto-suggest feature for station. A user should be able to see flights based on station code or location name. For example,
for Nashville (BNA), a user should be able to select flights to/from Nashville by entering the keywords BNA or Nashville. 

3. Provide two RESTful endpoints supporting the functionality listed in steps 1 and 2.

## Datasource

A zipped CSV file of flights is available in /data/flights.csv. Each row in the CSV file represents a flight.

## Tech Stack

This application uses an Angular frontend framework connected to a Python backend in order to allow the user to search for flights and return a table of flights depending on origin or destination. The frontend takes advantage of the Angular Material to display its components, and the python API uses fastAPI in order to fulfill requests.

## Install Requirements 

### API

To install requirements for the API, create a virtual environment and activate it, then install the requirements with:

```
pip install -r requirements.txt
```

### Frontend

In order to run the frontend Angular application, you must have Node and npm

Start by install npm with 

```
npm install
```

and add the Angular framework packages and Angular Material packages with 

```
npm install @angular/cli 
```

and 

```
ng add @angular/material
```

## Running the Application

To start the backend, navigate to the api directory and run the command:

```
uvicorn api:app --reload
```

To start the frontend, navigate to the flights-frontend directory and run the command:

```
ng s
```

By default, the API will be running on localhost:8000 while the frontend will be running on localhost:4200. 