
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './front/pages/Home';
import Articles from './front/pages/articulos';
import Categories from './front/pages/categorias';
import Types from './front/pages/tipos';
import Login from './front/pages/Login';
import Admin from './front/pages/Admin';
import AdminArticles from './front/pages/AdminArticles';
import AdminCategories from './front/pages/AdminCategories';
import AdminTypes from './front/pages/AdminTypes';
import './front/styles/floatingCards.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/articulos" element={<Articles />} />
          <Route path="/categorias" element={<Categories />} />
          <Route path="/tipos" element={<Types />} />
          <Route path="/login" element={<Login />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/admin/articles" element={<AdminArticles />} />
          <Route path="/admin/categories" element={<AdminCategories />} />
          <Route path="/admin/types" element={<AdminTypes />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
