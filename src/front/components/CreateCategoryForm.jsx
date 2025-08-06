import React, { useState } from 'react';
import axios from 'axios';

const CreateCategoryForm = ({ onCategoryCreated }) => {
  const [name, setName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/api/categories', { name });
      onCategoryCreated(response.data);
      setName('');
    } catch (error) {
      console.error('Error creating category:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Category</h2>
      <div>
        <label>Name</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </div>
      <button type="submit">Create</button>
    </form>
  );
};

export default CreateCategoryForm;
