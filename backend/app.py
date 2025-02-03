from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access the API

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodie_goodies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# FoodItem model
class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "image_url": self.image_url}

# ✅ Correct way to create tables in Flask 2.3+
with app.app_context():
    db.create_all()

# API Routes
@app.route('/api/food-items', methods=['GET'])
def get_food_items():
    food_items = FoodItem.query.all()
    return jsonify([item.to_dict() for item in food_items]), 200

# Sample route for signup
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    # Assuming you have a logic to handle signup here
    # You can return a response like:
    return jsonify({"message": "User signed up successfully!"}), 201

@app.route('/api/food-items', methods=['POST'])
def add_food_item():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    if "name" not in data or "price" not in data:
        return jsonify({"error": "Missing 'name' or 'price'"}), 400

    new_item = FoodItem(name=data["name"], price=data["price"], image_url=data.get("image_url"))
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

if __name__ == '__main__':
    app.run(debug=True)

