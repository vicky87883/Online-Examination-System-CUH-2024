import React from 'react';
import { Card, CardBody } from 'react-bootstrap';
import { useState } from 'react';
const TeacherLogin = () => {
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
    <div>
        <Card className="card-next">
      <CardBody>
      <h2>Teacher Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Email address</label>
          <input type="email" 
          className="form-control" 
          placeholder="Teacher Email" 
          value={username}
          onChange={handleUsernameChange}
          required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Password</label>
          <input type="password" 
          className="form-control" 
          placeholder="Teacher Password" 
          value={password}
          onChange={handlePasswordChange}
          required
          />
        </div>
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
      </CardBody>
      </Card>
    </div>
  );
};

export default TeacherLogin;
