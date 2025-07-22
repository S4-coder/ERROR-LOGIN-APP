import React, { useEffect, useState } from 'react';

function Dashboard() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetch('/api/errors/categories')
      .then(res => res.json())
      .then(data => setCategories(data))
      .catch(err => console.error('Failed to fetch categories:', err));
  }, []);

  return (
    <div>
      <h2>Error Categories</h2>
      <ul>
        {categories.map(category => (
          <li key={category}>{category}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
