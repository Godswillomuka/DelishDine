from app import db

class FoodItem(db.Model):
    __tablename__ = 'food_item'  # or use any other name you prefer
    __table_args__ = {'extend_existing': True}  # Add this line

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=True)

    # Add relationships, if necessary
    # Example: orders = db.relationship('OrderItem', backref='food_item', lazy=True)


class User(db.Model):
    __tablename__ = 'user'  # or use any other name you prefer
    __table_args__ = {'extend_existing': True}  # Add this line

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
    

class Order(db.Model):
    __tablename__ = 'order'  # or use any other name you prefer
    __table_args__ = {'extend_existing': True}  # Add this line

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "total_price": self.total_price}


class OrderItem(db.Model):
    __tablename__ = 'order_item'  # or use any other name you prefer
    __table_args__ = {'extend_existing': True}  # Add this line

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
