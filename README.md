Pizza Restaurant API
A RESTful API built with Flask, SQLAlchemy, and Flask-Migrate to manage pizza restaurants, pizzas, and their associations. This project follows the MVC pattern and includes models with validations, relationships, and cascading deletes. The API is tested using Postman and documented thoroughly below.
Project Overview
The API allows users to:

Retrieve a list of all restaurants and pizzas.
View details of a specific restaurant, including its associated pizzas.
Delete a restaurant and its related restaurant-pizza associations.
Create new restaurant-pizza associations with price validation.
Test all endpoints using a provided Postman collection.

No frontend is required; the focus is on a robust backend implementation.
Setup Instructions
Follow these steps to set up and run the project locally:

Clone the Repository:
git clone https://github.com/<your-username>/pizza-api-challenge.git
cd pizza-api-challenge


Set Up Virtual Environment:Install pipenv and required packages:
pip install pipenv
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell


Set Flask Environment Variable:
export FLASK_APP=server/app.py


Initialize Database:Create and apply migrations:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade


Seed Database:Populate the database with sample data:
python server/seed.py


Run the Application:Start the Flask development server:
flask run

The API will be available at http://127.0.0.1:5000.


Database Migration & Seeding

Migrations:
Generate new migrations: flask db migrate -m "message"
Apply migrations: flask db upgrade
Roll back migrations (if needed): flask db downgrade


Seeding:
Run python server/seed.py to clear existing data and populate the database with sample restaurants, pizzas, and restaurant-pizza associations.
The seed script ensures the database is ready for testing with meaningful data.



Project Structure
The project follows the MVC (Model-View-Controller) pattern:
pizza-api-challenge/
├── server/
│   ├── __init__.py
│   ├── app.py                # Flask app setup
│   ├── config.py             # Database configuration
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── restaurant.py     # Restaurant model
│   │   ├── pizza.py          # Pizza model
│   │   ├── restaurant_pizza.py # RestaurantPizza join table
│   ├── controllers/          # Route handlers
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   ├── restaurant_pizza_controller.py
│   ├── seed.py               # Database seeding script
├── migrations/               # Flask-Migrate migrations
├── challenge-1-pizzas.postman_collection.json # Postman collection
├── README.md                 # Project documentation

Route Summary
The API provides the following endpoints:



Method
Endpoint
Description



GET
/restaurants
Retrieve a list of all restaurants


GET
/restaurants/<id>
Get details of a specific restaurant and its pizzas


DELETE
/restaurants/<id>
Delete a restaurant and its associations


GET
/pizzas
Retrieve a list of all pizzas


POST
/restaurant_pizzas
Create a new restaurant-pizza association


Example Requests & Responses
GET /restaurants
Request:
GET http://127.0.0.1:5000/restaurants

Response (200 OK):
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Street 123",
    "pizzas": [
      {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]
  },
  {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "Broadway 456",
    "pizzas": [
      {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      }
    ]
  }
]

GET /restaurants/
Request:
GET http://127.0.0.1:5000/restaurants/1

Response (200 OK):
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Street 123",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

Response (404 Not Found):
{
  "error": "Restaurant not found"
}

DELETE /restaurants/
Request:
DELETE http://127.0.0.1:5000/restaurants/1

Response (204 No Content):

No body returned.Response (404 Not Found):

{
  "error": "Restaurant not found"
}

GET /pizzas
Request:
GET http://127.0.0.1:5000/pizzas

Response (200 OK):
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]

POST /restaurant_pizzas
Request:
POST http://127.0.0.1:5000/restaurant_pizzas
Content-Type: application/json

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2
}

Response (201 Created):
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "Broadway 456"
  }
}

Response (400 Bad Request, Invalid Price):
{
  "errors": ["Price must be between 1 and 30"]
}

Response (400 Bad Request, Invalid IDs):
{
  "errors": ["Restaurant or Pizza not found"]
}

Validation Rules

RestaurantPizza.price: Must be an integer between 1 and 30 (inclusive).
RestaurantPizza.restaurant_id: Must reference an existing Restaurant record.
RestaurantPizza.pizza_id: Must reference an existing Pizza record.
Cascading Deletes: Deleting a Restaurant automatically removes its associated RestaurantPizza records due to the cascade='all, delete-orphan' configuration.

Postman Testing
To test the API using Postman:

Import the Collection:

Open Postman.
Click Import > Upload Files.
Select challenge-1-pizzas.postman_collection.json from the project root.
Click Import.


Run the Flask App:Ensure the Flask server is running:
flask run


Execute Requests:

Navigate to the imported Pizza Restaurant API collection in Postman.
Run each request (e.g., Get All Restaurants, Create RestaurantPizza) to verify functionality.
Test edge cases, such as:
Retrieving a non-existent restaurant (GET /restaurants/999).
Creating a RestaurantPizza with an invalid price (price: 0 or price: 31).
Creating a RestaurantPizza with non-existent restaurant_id or pizza_id.




Verify Responses:Compare responses with the examples above to ensure correctness.


Troubleshooting

Database Errors:
Ensure FLASK_APP=server/app.py is set.
Verify the database URI in server/config.py (sqlite:///pizza.db).
Re-run migrations if needed: flask db upgrade.


Postman Issues:
Confirm the Flask app is running at http://127.0.0.1:5000.
Check that the database is seeded (python server/seed.py).


Validation Failures:
Review server/models/restaurant_pizza.py for price validation logic.
Ensure restaurant_id and pizza_id exist in the database before posting to /restaurant_pizzas.



Submission Checklist

 MVC folder structure implemented.
 Models (Restaurant, Pizza, RestaurantPizza) with validations and relationships.
 All required routes (GET /restaurants, GET /restaurants/<id>, DELETE /restaurants/<id>, GET /pizzas, POST /restaurant_pizzas) implemented.
 Postman collection (challenge-1-pizzas.postman_collection.json) provided and tests passing.
 Comprehensive README.md with setup, routes, examples, validations, and testing instructions.
 Database seeded with sample data via seed.py.
 Cascading deletes configured for Restaurant model.


# Pizza Restaurant API

A RESTful API built with Flask, SQLAlchemy, and Flask-Migrate to manage pizza restaurants, pizzas, and their associations. This project follows the MVC pattern and includes models with validations, relationships, and cascading deletes. The API is tested using Postman and documented thoroughly below.

## Project Overview

The API allows users to:
- Retrieve a list of all restaurants and pizzas.
- View details of a specific restaurant, including its associated pizzas.
- Delete a restaurant and its related restaurant-pizza associations.
- Create new restaurant-pizza associations with price validation.
- Test all endpoints using a provided Postman collection.

No frontend is required; the focus is on a robust backend implementation.

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/pizza-api-challenge.git
   cd pizza-api-challenge
   ```

2. **Set Up Virtual Environment:**
   Install pipenv and required packages:
   ```bash
   pip install pipenv
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell
   ```

3. **Set Flask Environment Variable:**
   ```bash
   export FLASK_APP=server/app.py
   ```

4. **Initialize Database:**
   Create and apply migrations:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Seed Database:**
   Populate the database with sample data:
   ```bash
   python server/seed.py
   ```

6. **Run the Application:**
   Start the Flask development server:
   ```bash
   flask run
   ```
   The API will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Database Migration & Seeding

- **Migrations:**
  - Generate new migrations: `flask db migrate -m "message"`
  - Apply migrations: `flask db upgrade`
  - Roll back migrations (if needed): `flask db downgrade`

- **Seeding:**
  - Run `python server/seed.py` to clear existing data and populate the database with sample restaurants, pizzas, and restaurant-pizza associations.
  - The seed script ensures the database is ready for testing with meaningful data.

## Project Structure

The project follows the MVC (Model-View-Controller) pattern:

```
pizza-api-challenge/
├── server/
│   ├── __init__.py
│   ├── app.py                # Flask app setup
│   ├── config.py             # Database configuration
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── restaurant.py     # Restaurant model
│   │   ├── pizza.py          # Pizza model
│   │   ├── restaurant_pizza.py # RestaurantPizza join table
│   ├── controllers/          # Route handlers
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   ├── restaurant_pizza_controller.py
│   ├── seed.py               # Database seeding script
├── migrations/               # Flask-Migrate migrations
├── challenge-1-pizzas.postman_collection.json # Postman collection
├── README.md                 # Project documentation
```

## Route Summary

The API provides the following endpoints:

| Method | Endpoint                | Description                                 |
|--------|-------------------------|---------------------------------------------|
| GET    | /restaurants            | Retrieve a list of all restaurants          |
| GET    | /restaurants/<id>       | Get details of a specific restaurant        |
| DELETE | /restaurants/<id>       | Delete a restaurant and its associations    |
| GET    | /pizzas                 | Retrieve a list of all pizzas               |
| POST   | /restaurant_pizzas      | Create a new restaurant-pizza association   |

## Example Requests & Responses

### GET /restaurants
**Request:**
```
GET http://127.0.0.1:5000/restaurants
```
**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Street 123",
    "pizzas": [
      {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]
  },
  {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "Broadway 456",
    "pizzas": [
      {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      }
    ]
  }
]
```

### GET /restaurants/<id>
**Request:**
```
GET http://127.0.0.1:5000/restaurants/1
```
**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Street 123",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
```
**Response (404 Not Found):**
```json
{
  "error": "Restaurant not found"
}
```

### DELETE /restaurants/<id>
**Request:**
```
DELETE http://127.0.0.1:5000/restaurants/1
```
**Response (204 No Content):**
No body returned.

**Response (404 Not Found):**
```json
{
  "error": "Restaurant not found"
}
```

### GET /pizzas
**Request:**
```
GET http://127.0.0.1:5000/pizzas
```
**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

### POST /restaurant_pizzas
**Request:**
```
POST http://127.0.0.1:5000/restaurant_pizzas
Content-Type: application/json

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2
}
```
**Response (201 Created):**
```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "Broadway 456"
  }
}
```
**Response (400 Bad Request, Invalid Price):**
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```
**Response (400 Bad Request, Invalid IDs):**
```json
{
  "errors": ["Restaurant or Pizza not found"]
}
```

## Validation Rules

- `RestaurantPizza.price`: Must be an integer between 1 and 30 (inclusive).
- `RestaurantPizza.restaurant_id`: Must reference an existing Restaurant record.
- `RestaurantPizza.pizza_id`: Must reference an existing Pizza record.
- **Cascading Deletes:** Deleting a Restaurant automatically removes its associated RestaurantPizza records due to the `cascade='all, delete-orphan'` configuration.

## Postman Testing

To test the API using Postman:

1. **Import the Collection:**
   - Open Postman.
   - Click Import > Upload Files.
   - Select `challenge-1-pizzas.postman_collection.json` from the project root.
   - Click Import.

2. **Run the Flask App:**
   Ensure the Flask server is running:
   ```bash
   flask run
   ```

3. **Execute Requests:**
   - Navigate to the imported Pizza Restaurant API collection in Postman.
   - Run each request (e.g., Get All Restaurants, Create RestaurantPizza) to verify functionality.
   - Test edge cases, such as:
     - Retrieving a non-existent restaurant (`GET /restaurants/999`).
     - Creating a RestaurantPizza with an invalid price (`price: 0` or `price: 31`).
     - Creating a RestaurantPizza with non-existent `restaurant_id` or `pizza_id`.

4. **Verify Responses:**
   - Compare responses with the examples above to ensure correctness.

## Troubleshooting

- **Database Errors:**
  - Ensure `FLASK_APP=server/app.py` is set.
  - Verify the database URI in `server/config.py` (`sqlite:///pizza.db`).
  - Re-run migrations if needed: `flask db upgrade`.

- **Postman Issues:**
  - Confirm the Flask app is running at [http://127.0.0.1:5000](http://127.0.0.1:5000).
  - Check that the database is seeded (`python server/seed.py`).

- **Validation Failures:**
  - Review `server/models/restaurant_pizza.py` for price validation logic.
  - Ensure `restaurant_id` and `pizza_id` exist in the database before posting to `/restaurant_pizzas`.

## Submission Checklist

- [x] MVC folder structure implemented.
- [x] Models (Restaurant, Pizza, RestaurantPizza) with validations and relationships.
- [x] All required routes (`GET /restaurants`, `GET /restaurants/<id>`, `DELETE /restaurants/<id>`, `GET /pizzas`, `POST /restaurant_pizzas`) implemented.
- [x] Postman collection (`challenge-1-pizzas.postman_collection.json`) provided and tests passing.
- [x] Comprehensive README.md with setup, routes, examples, validations, and testing instructions.
- [x] Database seeded with sample data via `seed.py`.
- [x] Cascading deletes configured for Restaurant model.
