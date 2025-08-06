import React from 'react';
import '../styles/components/Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>About ApiCultura</h3>
          <p>
            ApiCultura is your comprehensive resource for beekeeping and apiculture management.
            We provide tools and information to help beekeepers manage their apiaries effectively.
          </p>
        </div>

        <div className="footer-section">
          <h3>Quick Links</h3>
          <ul className="footer-links">
            <li><a href="/articulos">Articles</a></li>
            <li><a href="/categorias">Categories</a></li>
            <li><a href="/tipos">Types</a></li>
          </ul>
        </div>

        <div className="footer-section">
          <h3>Contact Us</h3>
          <p>
            Email: info@apicultura.com<br />
            Phone: (123) 456-7890
          </p>
          <div className="social-links">
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a>
          </div>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; {new Date().getFullYear()} ApiCultura. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
