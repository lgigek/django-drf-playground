# django-drf-playground

This project was initially created as an example to Construdelas' students.

It's a TO-DO list, that's not finished yet. 

## Running the project
This project uses [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/).

### Running the project
Simply run `docker-compose up --build app`. It'll be available at [http://localhost:8000](http://localhost:8000/). 

### Running the tests
Run `docker-compose up --build integration-tests`

## Project routes
As a to-do list, we have the users:
- POST /api/v1/users - Creates a user;
- GET /api/v1/users - List all users;
- GET /api/v1/users/<user_id> - Fetch a specific user;
- PATCH /api/v1/users/<user_id> - Not created yet;
- DELETE /api/v1/users/<user_id> - Not created yet;

And the tasks (routes not created yet).
