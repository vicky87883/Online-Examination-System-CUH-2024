import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import AdminLogin from './Login/AdminLogin';
import TeacherLogin from './Login/TeacherLogin';
import StudentLogin from './Login/StudentLogin';

const Login = () => {
  return (
    <div>
      <h2>Login</h2>
      <ul className="nav nav-tabs mb-4">
        <li className="nav-item">
          <Link to="/login/admin" className="nav-link">Admin</Link>
        </li>
        <li className="nav-item">
          <Link to="/login/teacher" className="nav-link">Teachers</Link>
        </li>
        <li className="nav-item">
          <Link to="/login/student" className="nav-link">Students</Link>
        </li>
      </ul>

      <Routes>
        <Route path="admin" element={<AdminLogin />} />
        <Route path="teacher" element={<TeacherLogin />} />
        <Route path="student" element={<StudentLogin />} />
      </Routes>
    </div>
  );
};

export default Login;
