import React, { useEffect, useState } from "react";
import FloatingCard from "../component/FloatingCard.jsx";
import Navbar from "../component/navbar.jsx";
import Footer from "../component/footer.jsx";
import { BACKEND_URL } from "../config";
import "../styles/floatingCards.css";
import "../styles/loading.css";
import "../styles/components/Navbar.css";
import "../styles/components/Footer.css";

const Home = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [showLogin, setShowLogin] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const fetchArticles = async () => {
      console.log('Fetching articles from:', `${BACKEND_URL}/api/articles`);
      try {
        const response = await fetch(`${BACKEND_URL}/api/articles`);
        console.log('Response status:', response.status);
        if (!response.ok) {
          throw new Error(`Failed to fetch articles (Status: ${response.status})`);
        }
        const data = await response.json();
        console.log('Received data:', data);
        setArticles(data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching articles:', err);
        setError(
          `Unable to load articles from ${BACKEND_URL}/api/articles. Error: ${err.message}`
        );
        setLoading(false);
      }
    };

    console.log('Component mounted, starting fetch...');
    fetchArticles();
  }, []);

  if (loading) {
    return (
      <div className="floating-cards-container">
        <div className="loading-message">
          Loading articles from {BACKEND_URL}...
          <div className="loading-spinner"></div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="floating-cards-container">
        <div className="error-message">
          <h2>Error Loading Articles</h2>
          <p>{error}</p>
          <code>Backend URL: {BACKEND_URL}</code>
        </div>
      </div>
    );
  }

  const handleLogin = () => {
    window.location.href = '/login';
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  const mainContent = () => {
    if (loading) {
      return (
        <div className="content-container">
          <div className="loading-message">
            Loading articles from {BACKEND_URL}...
            <div className="loading-spinner"></div>
          </div>
        </div>
      );
    }

    if (error) {
      return (
        <div className="content-container">
          <div className="error-message">
            <h2>Error Loading Articles</h2>
            <p>{error}</p>
            <code>Backend URL: {BACKEND_URL}</code>
          </div>
        </div>
      );
    }

    return (
      <div className="content-container">
        <div className="welcome-section">
          <h1>Welcome to ApiCultura</h1>
          <p>Your comprehensive resource for beekeeping and apiculture management</p>
        </div>
        <div className="floating-cards-container">
          {articles.length === 0 ? (
            <div className="no-articles-message">No articles found</div>
          ) : (
            articles.map((article) => (
              <FloatingCard
                key={article.id}
                title={article.title}
                description={article.content}
                image={article.image || "https://images.unsplash.com/photo-1582407947304-fd86f028f716?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80"}
              />
            ))
          )}
        </div>
      </div>
    );
  };

  return (
    <div className="app-container">
      <Navbar 
        onLoginClick={handleLogin}
        onLogoutClick={handleLogout}
        isLoggedIn={isLoggedIn}
      />
      {mainContent()}
      <Footer />
    </div>
  );
};

export default Home;