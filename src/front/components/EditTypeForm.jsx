import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EditTypeForm = ({ type, onTypeUpdated, onCancel }) => {
  const [name, setName] = useState('');

  useEffect(() => {
    if (type) {
      setName(type.name);
    }
  }, [type]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.put(`/api/types/${type.id}`, { name });
      onTypeUpdated(response.data);
    } catch (error) {
      console.error('Error updating type:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Edit Type</h2>
      <div>
        <label>Name</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </div>
      <button type="submit">Update</button>
      <button type="button" onClick={onCancel}>Cancel</button>
    </form>
  );
};

export default EditTypeForm;
