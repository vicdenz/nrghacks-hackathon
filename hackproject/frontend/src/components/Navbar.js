// components/Navbar.js

import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/" className="nav-home">Home</Link> {/* "Home" is separated */}
      <div className="nav-items">
        <Link to="/about" className="nav-item">About</Link>
        <Link to="/contact" className="nav-item">Contact</Link>
		<Link to="/login" className="nav-item">Log In</Link>
		<Link to="/sign-up" className="nav-item">Sign Up</Link>
        {/* Add more navigation links as needed */}
      </div>
    </nav>
  );
};

export default Navbar;
