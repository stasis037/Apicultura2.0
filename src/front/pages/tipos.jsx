import React from 'react';
import Navbar from '../component/navbar.jsx';
import Footer from '../component/footer.jsx';

const Types = () => {
  return (
    <div className="app-container">
      <Navbar />
      <div className="content-container">
        <div className="welcome-section">
          <h1>Types</h1>
          <p>Explore different types of beekeeping practices</p>
        </div>
        {/* Types content will go here */}
      </div>
      <Footer />
    </div>
  );
};

export default Types;
