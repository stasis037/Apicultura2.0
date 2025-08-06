import React from 'react';
import '../styles/floatingCards.css';

const FloatingCard = ({ title, description, image }) => (
  <div className="floating-card">
    <div className="card-image">
      <img src={image} alt={title} />
    </div>
    <div className="card-content">
      <h3 className="card-title">{title}</h3>
      <p className="card-description">{description}</p>
    </div>
  </div>
);

export default FloatingCard;
