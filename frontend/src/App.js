import React from "react";
import Navbar from "./components/Navbar";
import { Routes, Route } from "react-router-dom";  // Ensure these imports are correct
import FoodItems from "./pages/FoodItems";
import Home from "./pages/Home";
import Orders from "./pages/Orders";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/food-items" element={<FoodItems />} />
        <Route path="/orders" element={<Orders />} />
      </Routes>
    </div>
  );
}

export default App;






