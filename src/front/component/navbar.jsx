import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import '../styles/components/Navbar.css';

const Navbar = ({ onLoginClick, onLogoutClick, isLoggedIn }) => {
  const location = useLocation();
  const navigate = useNavigate();
  return (
    <nav className="navbar">
      <Link to="/" className="navbar-brand">
        <img src="/assets/bee-logo.svg" alt="ApiCultura Logo" />
        <span>ApiCultura</span>
      </Link>

      <div className="nav-links">
        <Link to="/" className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}>
          Home
        </Link>
        <Link to="/articulos" className={`nav-link ${location.pathname === '/articulos' ? 'active' : ''}`}>
          Articles
        </Link>
        <Link to="/categorias" className={`nav-link ${location.pathname === '/categorias' ? 'active' : ''}`}>
          Categories
        </Link>
        <Link to="/tipos" className={`nav-link ${location.pathname === '/tipos' ? 'active' : ''}`}>
          Types
        </Link>
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
