import { Link } from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <h1>DashDine</h1>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/food-items">Food Items</Link></li>
        <li><Link to="/orders">Orders</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
