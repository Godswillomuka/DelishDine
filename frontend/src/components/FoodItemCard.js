import React from 'react';

const FoodItemCard = ({ item, onUpdate, onDelete }) => {
  const handleDelete = () => {
    onDelete(item.id);
  };

  const handleUpdate = () => {
    const updatedItem = { name: 'Updated ' + item.name, price: item.price + 1 };
    onUpdate(item.id, updatedItem);
  };

  return (
    <div>
      <h2>{item.name}</h2>
      <p>Price: ${item.price}</p>
      <button onClick={handleUpdate}>Update</button>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default FoodItemCard;
