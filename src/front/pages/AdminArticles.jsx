import React, { useState, useEffect } from 'react';
import axios from 'axios';

import EditArticleForm from '../components/EditArticleForm';

import '../styles/pages/admin.css';

const AdminArticles = () => {
  const [articles, setArticles] = useState([]);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingArticle, setEditingArticle] = useState(null);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await axios.get('/api/articles');
        setArticles(response.data);
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    };

    fetchArticles();
  }, []);

  const handleArticleCreated = (newArticle) => {
    setArticles([...articles, newArticle]);
    setShowCreateForm(false);
  };

  const handleArticleUpdated = (updatedArticle) => {
    setArticles(
      articles.map((article) =>
        article.id === updatedArticle.id ? updatedArticle : article
      )
    );
    setEditingArticle(null);
  };

  const handleDelete = async (articleId) => {
    try {
      await axios.delete(`/api/articles/${articleId}`);
      setArticles(articles.filter((article) => article.id !== articleId));
    } catch (error) {
      console.error('Error deleting article:', error);
    }
  };

  return (
    <div className="admin-container">
      <h1>Manage Articles</h1>
      <button onClick={() => setShowCreateForm(!showCreateForm)}>
        {showCreateForm ? 'Cancel' : 'Create Article'}
      </button>
      {showCreateForm && <CreateArticleForm onArticleCreated={handleArticleCreated} />}
      {editingArticle && (
        <EditArticleForm
          article={editingArticle}
          onArticleUpdated={handleArticleUpdated}
          onCancel={() => setEditingArticle(null)}
        />
      )}
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {articles.map((article) => (
            <tr key={article.id}>
              <td>{article.title}</td>
              <td>
                <button onClick={() => setEditingArticle(article)}>Edit</button>
                <button onClick={() => handleDelete(article.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminArticles;
