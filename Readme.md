# FastAPI with Docker and SQLite for the API development

## Description

This is a simple API development using FastAPI, Docker and SQLite. The API is a simple operation of Createing User, Enrolling User, calling Mock Payment Route.
The API is developed using FastAPI and the database is SQLite. The API is containerized using Docker. The API is deployed in Google Cloud Run. The API is documented using Swagger UI.

## API DOCS with SwaggerUI can be found here
[https://yoga-enroller-eb3lbyeafa-em.a.run.app/docs]

## ER Diagram and Relationship

![image](https://github.com/subhadip001/yoga-enroller-api/assets/78922392/c4136758-09d7-46c5-af8a-4a806318d56e)


### Relationships:

- A User can have multiple Enrollments, but each Enrollment is associated with one User. This is a one-to-many relationship from User to Enrollment.
- A User can make multiple Payments, but each Payment is made by one User. This is a one-to-many relationship from User to Payment.
- An Enrollment can have multiple Payments, but each Payment is associated with one Enrollment. This is a one-to-many relationship from Enrollment to Payment.
- The  CheckConstraint in the Enrollment table ensures that the month is between 1 and 12.

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

## Mock Cloud Architecture

![image](https://github.com/subhadip001/yoga-enroller-api/assets/78922392/e4627dc5-8a7d-4509-b388-fae7f5df4dec)

- Services are implemented as endpoints
- Instead of AWS Lambda as shown in diagram Google Cloudrun with docker has been used


## Screenshots

![image](https://github.com/subhadip001/yoga-enroller-api/assets/78922392/df501763-27af-4a6e-be55-da9e5ccaf9eb)

## Future Scope of Improvement

1. Add a Authentication System
2. Add a Dashboard to view the status of enrollment to the user
3. Changing of the Batch by the user can be added in the Dashboard
4. Add a Admin Dashboard to view the status of enrollment of all the users
5. UI can be improved by adding animations and transitions
6. Adding CI/CD for deployment of the docker image on pushing to dockerhub to Cloudrun
7. Removing the CORS problem permanently by making the api in other tech stack like nodejs etc. Due to limited time i have not transferred the api to other stack after finding the error caused by CORS.
8. If Someone can find way to solve the CORS problem in Google Cloudrun then please Contribute.
9. Use of Kubernetes for auto management of containers for highly scalable app.

