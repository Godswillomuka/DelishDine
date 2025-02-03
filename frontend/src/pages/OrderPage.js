import React from 'react';
import { useLocation } from 'react-router-dom';
import styles from './styles'; // Import the styles

function OrderPage() {
  const location = useLocation();
  const { orders } = location.state || {}; // Get orders from state passed via React Router

  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Your Orders</h2>
      {orders && orders.length > 0 ? (
        <div>
          <ul style={styles.orderList}>
            {orders.map((order, index) => (
              <li key={index} style={styles.orderItem}>
                {order.name} - ${order.price}
              </li>
            ))}
          </ul>
          <p style={styles.orderText}>
            <strong>Total Cost:</strong> $
            {orders.reduce((total, item) => total + item.price, 0).toFixed(2)}
          </p>
        </div>
      ) : (
        <p style={styles.noOrdersText}>You haven't ordered anything yet.</p>
      )}
    </div>
  );
}

export default OrderPage;
