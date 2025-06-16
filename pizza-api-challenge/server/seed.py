# server/seed.py
from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from builtins import print, ValueError

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Dominion Pizza", address="Good Street 123")
    r2 = Restaurant(name="Kiki's Pizza", address="Broadway 456")
    db.session.add_all([r1, r2])

    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([p1, p2])

    db.session.commit()

    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p1.id)
    db.session.add_all([rp1, rp2, rp3])

    db.session.commit()
    print("Database seeded successfully!")

# Import controllers to register routes
from server.controllers.restaurant_controller import restaurants_bp
from server.controllers.pizza_controller import pizzas_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp

app.register_blueprint(restaurants_bp)
app.register_blueprint(pizzas_bp)
app.register_blueprint(restaurant_pizzas_bp)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, jsonify, request
from server.app import db
from server.models.pizza import Pizza

pizzas_bp = Blueprint('pizzas', __name__)

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