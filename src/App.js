import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Home from './pages/quizlist/Quiz';
import About from './pages/About';
import Contact from './pages/Contact';
import StudentLogin from './pages/Login/StudentLogin';
import TeacherLogin from './pages/Login/TeacherLogin';
import AdminLogin from './pages/Login/AdminLogin';
import Login from './pages/auth/Login';
import Signup from './pages/auth/Signup';
import AppLayout from './AppLayout';

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLogin = (email, password) => {
    if (email === 'student@example.com' && password === 'password') {
      setIsAuthenticated(true);
      return true;
    } else {
      alert('Invalid credentials');
      return false;
    }
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={<AppLayout isAuthenticated={isAuthenticated} />}>
          <Route index element={isAuthenticated ? <Home /> : <Navigate to="/login" />} />
          <Route path="about" element={<About />} />
          <Route path="contact" element={<Contact />} />
          <Route path="login/student" element={<StudentLogin />} />
          <Route path="login/teacher" element={<TeacherLogin />} />
          <Route path="login/admin" element={<AdminLogin />} />
          <Route path="login" element={<Login onLogin={handleLogin} />} />
          <Route path="signup" element={<Signup />} />
        </Route>
      </Routes>
    </Router>
  );
};

export default App;
