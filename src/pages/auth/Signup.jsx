import React from 'react';
import { Link } from 'react-router-dom';
import './Signup.css'; // Specific CSS file for signup styles
import BackgroundImage from '../../Assets/imgs/bg.jpg'; // Your background image
import FormImage from '../../Assets/imgs/login.jpg'; // Image for the left side of the form
import { useState } from 'react';
const Signup = () => {
  const [passwordVisible, setPasswordVisible] = useState(false);

  // Toggle the password visibility
  const togglePasswordVisibility = () => {
    setPasswordVisible(!passwordVisible);
  };
  return (
    <div className="auth-page" style={{ backgroundImage: `url(${BackgroundImage})` }}>
      <div className="auth-container">
        {/* Left Side Image */}
        <div className="auth-left">
          <img src={FormImage} alt="Signup visual" className="auth-image" />
        </div>
        {/* Signup Form */}
        <div className="auth-right">
          <h2>Signup</h2>
          <form>
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input type="text" className="form-control" id="username" placeholder="Enter username" />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email address</label>
              <input type="email" className="form-control" id="email" placeholder="Enter email" />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              {/* <input type="password" className="form-control" id="password" placeholder="Enter password" /> */}
              <div className="password-field">
                <input
                  type={passwordVisible ? 'text' : 'password'}
                  className="form-control"
                  placeholder="Enter your password"
                  style={{ paddingRight: '40px' }} // For icon spacing
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
            <button type="submit" className="btn btn-primary">Signup</button>
          </form>
          <div className="switch-link">
            Already have an account? <Link to="/login">Login</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Signup;
