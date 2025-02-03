// src/pages/UserPage.js

import React, { useEffect, useState } from 'react';

function UserPage() {
  const [user, setUser] = useState(null);

  // Simulate fetching user data on component mount
  useEffect(() => {
    // This would typically be fetched from your backend
    // For now, we'll assume the user is stored in localStorage or via context
    const storedUser = JSON.parse(localStorage.getItem('user'));
    if (storedUser) {
      setUser(storedUser);
    }
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div className="user-page">
      <h2>Welcome, {user.username}!</h2>
      <p>Your account details will appear here.</p>
      {/* You can add more user-related features, like order history, settings, etc. */}
    </div>
  );
}

export default UserPage;
