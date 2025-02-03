from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)  # Allow frontend to access the API

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DelishDine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# FoodItem model
class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    ingredients = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image_url": self.image_url,
            "description": self.description,
            "category": self.category,
            "ingredients": self.ingredients
        }

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {"id": self.id, "username": self.username}

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "total_price": self.total_price}

# OrderItem model
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "food_item_id": self.food_item_id,
            "quantity": self.quantity,
            "price": self.price
        }

# API Routes
@app.route('/api/food-items', methods=['GET'])
def get_food_items():
    food_items = FoodItem.query.all()
    return jsonify([item.to_dict() for item in food_items]), 200

@app.route('/api/food-items', methods=['POST'])
def add_food_item():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    if "name" not in data or "price" not in data:
        return jsonify({"error": "Missing 'name' or 'price'"}), 400

    new_item = FoodItem(
        name=data["name"],
        price=data["price"],
        image_url=data.get("image_url"),
        description=data.get("description"),
        category=data.get("category"),
        ingredients=data.get("ingredients")
    )
    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item.to_dict()), 201

@app.route('/api/food-items/<int:item_id>', methods=['PUT'])
def update_food_item(item_id):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    item = FoodItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    if "name" in data:
        item.name = data["name"]
    if "price" in data:
        item.price = data["price"]
    if "image_url" in data:
        item.image_url = data["image_url"]
    if "description" in data:
        item.description = data["description"]
    if "category" in data:
        item.category = data["category"]
    if "ingredients" in data:
        item.ingredients = data["ingredients"]

    db.session.commit()
    return jsonify(item.to_dict()), 200

@app.route('/api/food-items/<int:item_id>', methods=['DELETE'])
def delete_food_item(item_id):
    item = FoodItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": f"Item with ID {item_id} deleted successfully"}), 200

# Sample route for signup
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    # Assuming you have a logic to handle signup here
    return jsonify({"message": "User signed up successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
