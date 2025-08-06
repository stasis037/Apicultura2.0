import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CreateTypeForm from '../components/CreateTypeForm';
import EditTypeForm from '../components/EditTypeForm';
import '../styles/pages/admin.css';

const AdminTypes = () => {
  const [types, setTypes] = useState([]);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingType, setEditingType] = useState(null);

  useEffect(() => {
    const fetchTypes = async () => {
      try {
        const response = await axios.get('/api/types');
        setTypes(response.data);
      } catch (error) {
        console.error('Error fetching types:', error);
      }
    };

    fetchTypes();
  }, []);

  const handleTypeCreated = (newType) => {
    setTypes([...types, newType]);
    setShowCreateForm(false);
  };

  const handleTypeUpdated = (updatedType) => {
    setTypes(
      types.map((type) =>
        type.id === updatedType.id ? updatedType : type
      )
    );
    setEditingType(null);
  };

  const handleDelete = async (typeId) => {
    try {
      await axios.delete(`/api/types/${typeId}`);
      setTypes(types.filter((type) => type.id !== typeId));
    } catch (error) {
      console.error('Error deleting type:', error);
    }
  };

  return (
    <div>
      <h1>Manage Types</h1>
      <button onClick={() => setShowCreateForm(!showCreateForm)}>
        {showCreateForm ? 'Cancel' : 'Create Type'}
      </button>
      {showCreateForm && <CreateTypeForm onTypeCreated={handleTypeCreated} />}
      {editingType && (
        <EditTypeForm
          type={editingType}
          onTypeUpdated={handleTypeUpdated}
          onCancel={() => setEditingType(null)}
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
          {types.map((type) => (
            <tr key={type.id}>
              <td>{type.name}</td>
              <td>
                <button onClick={() => setEditingType(type)}>Edit</button>
                <button onClick={() => handleDelete(type.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminTypes;
