import React, { useEffect, useState } from 'react';

function ErrorList({ onSelectError }) {
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    fetch('/api/errors')
      .then(res => res.json())
      .then(data => setErrors(data))
      .catch(err => console.error('Failed to fetch errors:', err));
  }, []);

  return (
    <div>
      <h2>Error Logs</h2>
      <ul>
        {errors.map(error => (
          <li key={error.id} onClick={() => onSelectError(error)} style={{cursor: 'pointer', marginBottom: '10px'}}>
            <strong>[{error.category}]</strong> {error.message} <em>({new Date(error.timestamp).toLocaleString()})</em>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ErrorList;
