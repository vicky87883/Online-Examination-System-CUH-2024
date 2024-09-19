import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Signup.css';
import BackgroundImage from '../../Assets/imgs/bg.jpg';
import FormImage from '../../Assets/imgs/login.jpg';

const StudentLogin = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordVisible, setPasswordVisible] = useState(false);
  const navigate = useNavigate(); // <-- useNavigate hook

  const togglePasswordVisibility = () => {
    setPasswordVisible(!passwordVisible);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const loginSuccess = onLogin(email, password); // Call onLogin to validate the user
    
    // If login is successful, navigate to the home page
    if (loginSuccess) {
      navigate('/'); // Redirect to the home page after login
    }
  };

  return (
    <div className="auth-page" style={{ backgroundImage: `url(${BackgroundImage})` }}>
      <div className="auth-container">
        <div className="auth-left">
          <img src={FormImage} alt="Login visual" className="auth-image" />
        </div>
        <div className="auth-right">
          <h2>Login</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email address</label>
              <input
                type="email"
                className="form-control"
                id="email"
                placeholder="Enter email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <div className="password-field">
                <input
                  type={passwordVisible ? 'text' : 'password'}
                  className="form-control"
                  id="password"
                  placeholder="Enter your password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  style={{ paddingRight: '40px' }}
                />
                <span
                  onClick={togglePasswordVisibility}
                  style={{
                    position: 'absolute',
                    right: '10px',
                    top: '50%',
                    transform: 'translateY(-50%)',
                    cursor: 'pointer',
                  }}
                >
                  {passwordVisible ? 'Hide' : 'Show'}
                </span>
              </div>
            </div>
            <button type="submit" className="btn btn-primary">Login</button>
          </form>
          <div className="switch-link">
            Don't have an account? <Link to="/signup">Sign up</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentLogin;
