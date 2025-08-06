import React from "react";
import "../styles/floatingCards.css";

const FloatingCard = ({ title, description, image }) => (
  <div className="floating-card">
    <div className="floating-card-image-container">
      {image && <img src={image} alt={title} className="floating-card-img" />}
    </div>
    <div className="floating-card-content">
      <h3 className="floating-card-title">{title}</h3>
      <p className="floating-card-description">
        {description.length > 150 ? `${description.substring(0, 150)}...` : description}
      </p>
      <button className="floating-card-button">Read More</button>
    </div>
  </div>
);

export default FloatingCard;
