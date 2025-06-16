# server/controllers/restaurant_controller.py
from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurants_bp = Blueprint('restaurants', __name__)
pizzas_bp = Blueprint('pizzas', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    return jsonify(restaurant.to_dict())

@restaurants_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

@pizzas_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@pizzas_bp.route('/pizzas/<int:id>', methods=['GET'])
def get_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({'error': 'Pizza not found'}), 404
    return jsonify(pizza.to_dict())

@pizzas_bp.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()
    name = data.get('name')
    ingredients = data.get('ingredients')
    if not name or not ingredients:
        return jsonify({'error': 'Missing name or ingredients'}), 400
    pizza = Pizza(name=name, ingredients=ingredients)
    db.session.add(pizza)
    db.session.commit()
    return jsonify(pizza.to_dict()), 201

@pizzas_bp.route('/pizzas/<int:id>', methods=['PUT'])
def update_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({'error': 'Pizza not found'}), 404
    data = request.get_json()
    pizza.name = data.get('name', pizza.name)
    pizza.ingredients = data.get('ingredients', pizza.ingredients)
    db.session.commit()
    return jsonify(pizza.to_dict())

@pizzas_bp.route('/pizzas/<int:id>', methods=['DELETE'])
def delete_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({'error': 'Pizza not found'}), 404
    db.session.delete(pizza)
    db.session.commit()
    return '', 204