import React from 'react';

function ErrorDetails({ error }) {
  if (!error) {
    return <div>Select an error to see details</div>;
  }

  return (
    <div>
      <h2>Error Details</h2>
      <p><strong>ID:</strong> {error.id}</p>
      <p><strong>Category:</strong> {error.category}</p>
      <p><strong>Message:</strong> {error.message}</p>
      <p><strong>Timestamp:</strong> {new Date(error.timestamp).toLocaleString()}</p>
      <p><strong>Metadata:</strong> <pre>{JSON.stringify(error.metadata, null, 2)}</pre></p>
    </div>
  );
}

export default ErrorDetails;
