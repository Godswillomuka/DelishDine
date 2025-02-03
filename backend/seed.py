from app import app, db
from models import FoodItem, User, Order, OrderItem

def seed_database():
    with app.app_context():  # Ensure we use the app context
        print("Seeding database...")

        # Delete existing data
        db.session.query(OrderItem).delete()
        db.session.query(Order).delete()
        db.session.query(FoodItem).delete()
        db.session.query(User).delete()
        db.session.commit()

        # Sample food data
        food_items = [
            {"name": "Cheeseburger", "description": "Juicy beef patty with cheese.", "price": 8.99, "image_url": "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600", "category": "Burger", "ingredients": "Beef, Cheese, Lettuce, Tomato"},
            {"name": "Margherita Pizza", "description": "Tomatoes, basil, and mozzarella.", "price": 12.50, "image_url": "https://images.pexels.com/photos/2147491/pexels-photo-2147491.jpeg?auto=compress&cs=tinysrgb&w=600", "category": "Pizza", "ingredients": "Tomato, Mozzarella, Basil"},
            {"name": "Caesar Salad", "description": "Lettuce with Caesar dressing.", "price": 7.99, "image_url": "https://images.pexels.com/photos/5446518/pexels-photo-5446518.jpeg?auto=compress&cs=tinysrgb&w=600", "category": "Salad", "ingredients": "Lettuce, Caesar Dressing, Croutons"},
            {"name": "Sushi Platter", "description": "Assorted sushi rolls.", "price": 15.99, "image_url": "https://images.pexels.com/photos/1148086/pexels-photo-1148086.jpeg?auto=compress&cs=tinysrgb&w=600", "category": "Sushi", "ingredients": "Rice, Fish, Seaweed"},
            {"name": "Spaghetti Carbonara", "description": "Pasta with pancetta and parmesan.", "price": 10.99, "image_url": "https://images.pexels.com/photos/128408/pexels-photo-128408.jpeg?auto=compress&cs=tinysrgb&w=600", "category": "Pasta", "ingredients": "Pasta, Pancetta, Parmesan, Eggs"}
        ]

        # Add new food items
        for food in food_items:
            new_food = FoodItem(
                name=food["name"],
                description=food["description"],
                price=food["price"],
                image_url=food["image_url"],
                category=food["category"],
                ingredients=food["ingredients"]
            )
            db.session.add(new_food)

        # Sample user data
        users = [
            {"username": "john_doe"},
            {"username": "jane_doe"}
        ]

        # Add new users
        for user in users:
            new_user = User(username=user["username"])
            db.session.add(new_user)

        # Commit users and food items
        db.session.commit()

        # Sample order data
        orders = [
            {"user_id": 1, "total_price": 22.48, "items": [(1, 2), (2, 1)]},  # John Doe orders 2 Cheeseburgers and 1 Margherita Pizza
            {"user_id": 2, "total_price": 15.99, "items": [(4, 1)]}  # Jane Doe orders 1 Sushi Platter
        ]

        # Add new orders and order items
        for order in orders:
            new_order = Order(user_id=order["user_id"], total_price=order["total_price"])
            db.session.add(new_order)
            db.session.commit()  # Commit first to generate the order ID for order items

            for food_item_id, quantity in order["items"]:
                food_item = FoodItem.query.get(food_item_id)
                order_item = OrderItem(order_id=new_order.id, food_item_id=food_item.id, quantity=quantity, price=food_item.price)
                db.session.add(order_item)

        db.session.commit()
        print("Database seeding complete!")

# Run the seed function
if __name__ == "__main__":
    seed_database()
