import React from 'react';
import { Card } from 'react-bootstrap';
import { useState } from 'react';
const AdminLogin = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };
  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle login logic here, e.g., send data to an API
    console.log('Username:', username);
    console.log('Password:', password);
  };
  return (
    <Card className="card-next">
      <Card.Body>
        <h2>Admin Login</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label"> Email address</label>
            <div>
              <input
                type="text"
                value={username}
                onChange={handleUsernameChange}
                className="form-control"
                placeholder="Admin Email"
                required
              />
            </div>
          </div>
          <div className="mb-3">
            <label className="form-label"> Password</label>
            <div>
              <input type="password"
                value={password}
                onChange={handlePasswordChange}
                className="form-control"
                placeholder="Admin Password" 
                required
                />
            </div>
          </div>
          <button type="submit" className="btn btn-primary">Login</button>
        </form>
      </Card.Body>
    </Card>
  );
};

export default AdminLogin;
