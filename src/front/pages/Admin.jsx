import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../component/navbar.jsx';
import Footer from '../component/footer.jsx';
import '../styles/pages/Admin.css';
import '../styles/pages/admin.css';
import axios from 'axios';

const Admin = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const checkAuth = async () => {
      try {
        // Attempt to access a protected route (e.g., get articles) to check authentication
        await axios.get('/api/articles'); 
      } catch (error) {
        // If authentication fails, redirect to login
        navigate('/login');
      }
    };
    checkAuth();
  }, [navigate]);

  const handleLogout = async () => {
    try {
      await axios.post('/api/auth/logout');
      navigate('/login');
    } catch (error) {
      console.error('Error logging out:', error);
    }
  };

  return (
    <div className="app-container">
      <Navbar isLoggedIn={true} />
      <div className="admin-container">
        <div className="admin-header">
          <h1>Admin Panel</h1>
          <p>Manage your apiculture content</p>
          <button onClick={handleLogout} className="logout-button">Logout</button>
        </div>
        <div className="admin-grid">
          <div className="admin-card">
            <h3>Articles</h3>
            <p>Manage your articles</p>
            <button onClick={() => navigate('/admin/articles')}>Manage Articles</button>
          </div>
          <div className="admin-card">
            <h3>Categories</h3>
            <p>Organize your content</p>
            <button onClick={() => navigate('/admin/categories')}>Manage Categories</button>
          </div>
          <div className="admin-card">
            <h3>Types</h3>
            <p>Define beekeeping types</p>
            <button onClick={() => navigate('/admin/types')}>Manage Types</button>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Admin;
