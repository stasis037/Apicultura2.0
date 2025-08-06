import React from 'react';
import Navbar from '../component/navbar.jsx';
import Footer from '../component/footer.jsx';

const Categories = () => {
  return (
    <div className="app-container">
      <Navbar />
      <div className="content-container">
        <div className="welcome-section">
          <h1>Categories</h1>
          <p>Browse articles by category</p>
        </div>
        {/* Categories content will go here */}
      </div>
      <Footer />
    </div>
  );
};

export default Categories;
