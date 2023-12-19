# FastAPI with Docker and SQLite for the API development

## Description

This is a simple API development using FastAPI, Docker and SQLite. The API is a simple operation of Createing User, Enrolling User, calling Mock Payment Route.
The API is developed using FastAPI and the database is SQLite. The API is containerized using Docker. The API is deployed in Google Cloud Run. The API is documented using Swagger UI.

## Features

- Create User
- Enroll User
- Mock Payment

## Tech Stack

- FastAPI
- Docker
- SQLite
- Swagger UI

## Problems Occured

- The deployed (in Cloudrun) API is not working in the client application because of CORS problem in FASTAPI. The API is working fine in local machine. The problem is with the database connection.

- The deployed API can be tested using Postman or Swagger UI. But the client application is not able to access the API because of CORS problem.

- Using CORS middleware in FASTAPI or allowing wildcard origin in FASTAPI or applying some other possible solutions are also not working.

## Possible Solutions

- People have faced the similar problem very much in fastapi and there are some solutions available in the internet. But none of them are working for me.

- The possible solution is to use some other language or framework for the API development such as NodeJS with ExpressJS as the problem is with FASTAPI i think.

## With Docker

## Requirements

- Docker
- Docker Compose

## How to run

1. Clone this repository
2. Run `docker-compose up --build`
3. Access `http://localhost:8000/docs` to see the API documentation

## Without Docker

## Requirements

- Python 3.11
- pip
- virtualenv

## How to run

1. Clone this repository
2. Create a virtualenv with `python3 -m venv venv`
3. Activate the virtualenv with `source venv/bin/activate`
4. Install the dependencies with `pip install -r requirements.txt`
5. Run `uvicorn main:app --reload --port=8000 --host=0.0.0.0`

## API Documentation
