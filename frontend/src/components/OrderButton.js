import React from 'react';

function OrderButton({ onOrder }) {
  return (
    <button onClick={onOrder}>Order Now</button>
  );
}

export default OrderButton;
