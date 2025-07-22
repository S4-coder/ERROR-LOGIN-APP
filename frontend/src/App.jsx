import React, { useState } from 'react';
import ErrorList from './components/ErrorList';
import ErrorDetails from './components/ErrorDetails';
import Dashboard from './components/Dashboard';

function App() {
  const [selectedError, setSelectedError] = useState(null);

  return (
    <div style={{ display: 'flex', padding: '20px' }}>
      <div style={{ flex: 1, marginRight: '20px' }}>
        <Dashboard />
        <ErrorList onSelectError={setSelectedError} />
      </div>
      <div style={{ flex: 2 }}>
        <ErrorDetails error={selectedError} />
      </div>
    </div>
  );
}

export default App;
