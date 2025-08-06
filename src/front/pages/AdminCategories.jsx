import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CreateCategoryForm from '../components/CreateCategoryForm';
import EditCategoryForm from '../components/EditCategoryForm';

import '../styles/pages/admin.css';

const AdminCategories = () => {
  const [categories, setCategories] = useState([]);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingCategory, setEditingCategory] = useState(null);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await axios.get('/api/categories');
        setCategories(response.data);
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    fetchCategories();
  }, []);

  const handleCategoryCreated = (newCategory) => {
    setCategories([...categories, newCategory]);
    setShowCreateForm(false);
  };

  const handleCategoryUpdated = (updatedCategory) => {
    setCategories(
      categories.map((category) =>
        category.id === updatedCategory.id ? updatedCategory : category
      )
    );
    setEditingCategory(null);
  };

  const handleDelete = async (categoryId) => {
    try {
      await axios.delete(`/api/categories/${categoryId}`);
      setCategories(categories.filter((category) => category.id !== categoryId));
    } catch (error) {
      console.error('Error deleting category:', error);
    }
  };

  return (
    <div className="admin-container">
      <h1>Manage Categories</h1>
      <button onClick={() => setShowCreateForm(!showCreateForm)}>
        {showCreateForm ? 'Cancel' : 'Create Category'}
      </button>
      {showCreateForm && <CreateCategoryForm onCategoryCreated={handleCategoryCreated} />}
      {editingCategory && (
        <EditCategoryForm
          category={editingCategory}
          onCategoryUpdated={handleCategoryUpdated}
          onCancel={() => setEditingCategory(null)}
        />
      )}
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {categories.map((category) => (
            <tr key={category.id}>
              <td>{category.name}</td>
              <td>
                <button onClick={() => setEditingCategory(category)}>Edit</button>
                <button onClick={() => handleDelete(category.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminCategories;
