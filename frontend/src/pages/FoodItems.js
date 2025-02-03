import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import OrderButton from '../components/OrderButton';
import styles from './styles'; // Import styles from styles.js

function FoodItems() {
  const [foodItems, setFoodItems] = useState([]);
  const [newFoodItem, setNewFoodItem] = useState({
    name: '',
    description: '',
    price: '',
    image_url: '',
  });
  const [orders, setOrders] = useState([]); // State to track orders

  const navigate = useNavigate(); // Hook to navigate between pages

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/food-items')
      .then((response) => response.json())
      .then((data) => {
        setFoodItems(data);
      })
      .catch((error) => console.error('Error fetching food items:', error));
  }, []);

  const handleOrder = (foodItemId) => {
    const orderedItem = foodItems.find((food) => food.id === foodItemId);
    if (orderedItem) {
      setOrders([...orders, orderedItem]);
      alert(`Order placed for ${orderedItem.name}`);
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setNewFoodItem({ ...newFoodItem, [name]: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch('http://127.0.0.1:5000/api/food-items', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newFoodItem),
    })
      .then((response) => response.json())
      .then((data) => {
        setFoodItems([...foodItems, data]); // Add the new food item to the list
        setNewFoodItem({
          name: '',
          description: '',
          price: '',
          image_url: '',
        });

        // After adding, navigate to OrderPage and pass orders
        navigate('/orders', { state: { orders: [...orders, data] } });
      })
      .catch((error) => console.error('Error adding food item:', error));
  };

  const handleGoToOrderPage = () => {
    // Navigate to the order page and pass the orders via state
    navigate('/orders', { state: { orders } });
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Food Menu</h2>

      <div style={styles.foodItemsContainer}>
        {foodItems.length > 0 ? (
          foodItems.map((foodItem) => (
            <div key={foodItem.id} style={styles.foodItem}>
              <img src={foodItem.image_url} alt={foodItem.name} style={styles.foodImage} />
              <h3 style={styles.foodName}>{foodItem.name}</h3>
              <p style={styles.foodDescription}>{foodItem.description}</p>
              <p style={styles.foodPrice}><strong>Price:</strong> ${foodItem.price}</p>
              <OrderButton onOrder={() => handleOrder(foodItem.id)} />
            </div>
          ))
        ) : (
          <p>Loading food items...</p>
        )}
      </div>

      <h3 style={styles.addNewFoodHeading}>Add New Food Item</h3>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          name="name"
          value={newFoodItem.name}
          onChange={handleInputChange}
          placeholder="Food Name"
          required
          style={styles.input}
        />
        <input
          type="text"
          name="description"
          value={newFoodItem.description}
          onChange={handleInputChange}
          placeholder="Food Description"
          required
          style={styles.input}
        />
        <input
          type="number"
          name="price"
          value={newFoodItem.price}
          onChange={handleInputChange}
          placeholder="Food Price"
          required
          style={styles.input}
        />
        <input
          type="text"
          name="image_url"
          value={newFoodItem.image_url}
          onChange={handleInputChange}
          placeholder="Image URL"
          required
          style={styles.input}
        />
        <button type="submit" style={styles.submitButton}>Add Food Item</button>
      </form>

      <div style={styles.orderSummary}>
        <h3>Your Orders</h3>
        {orders.length > 0 ? (
          <div>
            <p style={styles.orderText}>Total Orders: {orders.length}</p>
            <ul style={styles.orderList}>
              {orders.map((order, index) => (
                <li key={index} style={styles.orderItem}>
                  {order.name} - ${order.price}
                </li>
              ))}
            </ul>
            <p style={styles.orderText}>
              <strong>Total Cost: </strong>${orders.reduce((total, item) => total + item.price, 0).toFixed(2)}
            </p>
            <button onClick={handleGoToOrderPage} style={styles.viewOrderButton}>
              Go to Order Page
            </button>
          </div>
        ) : (
          <p style={styles.noOrdersText}>No orders placed yet.</p>
        )}
      </div>
    </div>
  );
}

export default FoodItems;



