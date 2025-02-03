import React, { useState } from 'react';

const FoodItemForm = ({ onAddFoodItem }) => {
  const [name, setName] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const newFoodItem = { name, price: parseFloat(price) };
    onAddFoodItem(newFoodItem);
    setName('');
    setPrice('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add New Food Item</h2>
      <div>
        <label>Name:</label>
        <input 
          type="text" 
          value={name} 
          onChange={(e) => setName(e.target.value)} 
        />
      </div>
      <div>
        <label>Price:</label>
        <input 
          type="number" 
          value={price} 
          onChange={(e) => setPrice(e.target.value)} 
        />
      </div>
      <button type="submit">Add Food Item</button>
    </form>
  );
};

export default FoodItemForm;
