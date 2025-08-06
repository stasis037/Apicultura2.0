import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/components/Navbar.css';
import logoBee from '../img/logobee.png';

const Navbar = ({ onLoginClick, onLogoutClick, isLoggedIn }) => {
  return (
    <nav className="navbar">
      <Link to="/" className="navbar-brand">
        <img src={logoBee} alt="ApiCultura Logo" />
        <span>ApiCultura</span>
      </Link>

      <div className="nav-links">
        <Link to="/" className="nav-link">Home</Link>
        <Link to="/articulos" className="nav-link">Articles</Link>
        <Link to="/categorias" className="nav-link">Categories</Link>
        <Link to="/tipos" className="nav-link">Types</Link>
      </div>

      <div className="auth-buttons">
        {isLoggedIn ? (
          <button onClick={onLogoutClick} className="auth-button logout-button">
            Logout
          </button>
        ) : (
          <button onClick={onLoginClick} className="auth-button login-button">
            Login
          </button>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
