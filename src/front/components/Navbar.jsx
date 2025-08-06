import React from 'react';
import './Navbar.css';

const Navbar = ({ onLoginClick, isLoggedIn, onLogoutClick }) => {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <img 
          src="/img/logobee.png" 
          alt="Apicultura Logo" 
          className="navbar-logo"
        />
        <span className="navbar-title">ApiCultura</span>
      </div>
      <div className="navbar-menu">
        <a href="/" className="navbar-link">Home</a>
        <a href="/articles" className="navbar-link">Articles</a>
        <a href="/about" className="navbar-link">About</a>
      </div>
      <div className="navbar-auth">
        {isLoggedIn ? (
          <button onClick={onLogoutClick} className="auth-button logout">
            Logout
          </button>
        ) : (
          <button onClick={onLoginClick} className="auth-button login">
            Login
          </button>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
