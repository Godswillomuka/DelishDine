from app import app, db
from models import FoodItem

def seed_database():
    with app.app_context():  # Ensure we use the app context
        print("Seeding database...")

        # Delete existing data
        db.session.query(FoodItem).delete()
        db.session.commit()

        # Sample food data
        food_items = [
            {"name": "Cheeseburger", "description": "Juicy beef patty with cheese.", "price": 8.99, "image_url": "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600"},
            {"name": "Margherita Pizza", "description": "Tomatoes, basil, and mozzarella.", "price": 12.50, "image_url": "https://images.pexels.com/photos/2147491/pexels-photo-2147491.jpeg?auto=compress&cs=tinysrgb&w=600"},
            {"name": "Caesar Salad", "description": "Lettuce with Caesar dressing.", "price": 7.99, "image_url": "https://images.pexels.com/photos/5446518/pexels-photo-5446518.jpeg?auto=compress&cs=tinysrgb&w=600"},
            {"name": "Sushi Platter", "description": "Assorted sushi rolls.", "price": 15.99, "image_url": "https://images.pexels.com/photos/1148086/pexels-photo-1148086.jpeg?auto=compress&cs=tinysrgb&w=600"},
            {"name": "Spaghetti Carbonara", "description": "Pasta with pancetta and parmesan.", "price": 10.99, "image_url": "https://images.pexels.com/photos/128408/pexels-photo-128408.jpeg?auto=compress&cs=tinysrgb&w=600"}
        ]

        # Add new food items
        for food in food_items:
            new_food = FoodItem(
                name=food["name"],
                price=food["price"],
                image_url=food["image_url"]
            )
            db.session.add(new_food)

        db.session.commit()
        print("Database seeding complete!")

# Run the seed function
if __name__ == "__main__":
    seed_database()
