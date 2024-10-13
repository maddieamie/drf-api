# Things API Project

## Overview

This project is a custom version of the Things API demo, built with Django and PostgreSQL. It includes a model for managing various resources while utilizing Docker for containerization.

## Features

- Dockerized Django application
- PostgreSQL as the database
- RESTful API using Django REST Framework
- Custom user model that extends the basic and abstract user classes from Django

## Setup Instructions

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine
- Basic knowledge of Docker and Django

**Create a .env File**
Create a .env file in the root of the project directory with the following content:

```
POSTGRES_DB=myapp_db
POSTGRES_USER=myapp_user
POSTGRES_PASSWORD=my_secure_password
```

**Build and Run the Docker Container**
Build the Docker images and start the containers:


`docker-compose up --build`

**Run migrations to set up the database:**

`docker-compose exec web python manage.py migrate`

**Create a superuser for accessing the Django admin:**

`docker-compose exec web python manage.py createsuperuser`

**Access the application:**

- Open your web browser and go to http://localhost:8000 to see the API.
- Access the Django admin at http://localhost:8000/admin and log in with the superuser credentials.

## Testing
Run the tests using the following command:


`docker-compose exec web python manage.py test`

**User Acceptance Tests**

The provided unit tests are modified to work with the custom application. Ensure that all tests pass to verify that the application is functioning as expected.

