import React from 'react';
import Navbar from '../component/navbar.jsx';
import Footer from '../component/footer.jsx';

const Articles = () => {
  return (
    <div className="app-container">
      <Navbar />
      <div className="content-container">
        <div className="welcome-section">
          <h1>Articles</h1>
          <p>Browse through our collection of beekeeping articles</p>
        </div>
        {/* Article content will go here */}
      </div>
      <Footer />
    </div>
  );
};

export default Articles;
