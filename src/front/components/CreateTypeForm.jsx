import React, { useState } from 'react';
import axios from 'axios';

const CreateTypeForm = ({ onTypeCreated }) => {
  const [name, setName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/api/types', { name });
      onTypeCreated(response.data);
      setName('');
    } catch (error) {
      console.error('Error creating type:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Type</h2>
      <div>
        <label>Name</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </div>
      <button type="submit">Create</button>
    </form>
  );
};

export default CreateTypeForm;
