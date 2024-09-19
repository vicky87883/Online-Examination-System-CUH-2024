import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, useLocation, Link } from 'react-router-dom';
import { Navbar, Nav, Button, Container, Dropdown, Badge, Form } from 'react-bootstrap';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import StudentLogin from './pages/Login/StudentLogin';
import TeacherLogin from './pages/Login/TeacherLogin';
import AdminLogin from './pages/Login/AdminLogin';
import Login from './pages/auth/Login';
import Signup from './pages/auth/Signup';
import './App.css';
import Logo from './Assets/imgs/logo.jpg'; 
import Favicon from './Assets/imgs/favicon.jpg'; 
import Avatar from './Assets/imgs/avatar.webp';
const AppLayout = ({ children, isAuthenticated, toggleSidebar, sidebarCollapsed }) => {
  const location = useLocation();
  const [loginDropdownOpen, setLoginDropdownOpen] = useState(false);

  const isAuthPage = location.pathname === '/login' || location.pathname === '/signup';

  const toggleLoginDropdown = () => {
    setLoginDropdownOpen(!loginDropdownOpen);
  };

  return (
    <div className="d-flex">
      {!isAuthPage && (
        <nav className={`bg-dark text-white p-3 sidebar ${sidebarCollapsed ? 'collapsed' : ''}`}>
          <div className="logo-section text-center mb-3">
            <Link to="/">
              {!sidebarCollapsed ? (
                <img src={Logo} alt="Logo" className="logo-img" style={{ maxWidth: '100%', height: '50px' }} />
              ) : (
                <img src={Favicon} alt="Favicon" className="favicon-img" style={{ maxWidth: '50px', height: '50px' }} />
              )}
            </Link>
          </div>

          <ul className="nav flex-column">
            <li className="nav-item">
              <Link to="/" className="nav-link text-white">
                <i className="bi bi-house s-icon"></i> {!sidebarCollapsed && 'Dashboard'}
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/about" className="nav-link text-white">
                <i className="bi bi-info-circle s-icon"></i> {!sidebarCollapsed && 'About'}
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/contact" className="nav-link text-white">
                <i className="bi bi-envelope s-icon"></i> {!sidebarCollapsed && 'Contact'}
              </Link>
            </li>
            <li className="nav-item">
              <div className="nav-link text-white" onClick={toggleLoginDropdown} style={{ cursor: 'pointer' }}>
                <i className="bi bi-key s-icon"></i> {!sidebarCollapsed && 'Login'}
                <i className={`bi ${loginDropdownOpen ? 'bi-caret-up-fill' : 'bi-caret-down-fill'}`}></i>
              </div>
              {loginDropdownOpen && (
                <ul className="nav flex-column ms-3">
                  <li className="nav-item">
                    <Link to="/login/student" className="nav-link text-white">
                      Student Login
                    </Link>
                  </li>
                  <li className="nav-item">
                    <Link to="/login/teacher" className="nav-link text-white">
                      Teacher Login
                    </Link>
                  </li>
                  <li className="nav-item">
                    <Link to="/login/admin" className="nav-link text-white">
                      Admin Login
                    </Link>
                  </li>
                </ul>
              )}
            </li>
          </ul>
        </nav>
      )}

      <div className="w-100">
        {!isAuthPage && (
          <Navbar bg="light" expand="lg" className="mb-4">
            <Container>
              <Button classname="toggle-btn" variant="outline-secondary" onClick={toggleSidebar} className="me-3">
                <i className="bi bi-list"></i>
              </Button>
              <Navbar.Brand className="d-lg-none">
                <img src={Logo} alt="Logo" style={{ height: '40px' }} />
              </Navbar.Brand>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                  <Form className="d-flex search-bar">
                    <Form.Control type="search" placeholder="Search..." className="me-2 search-input" aria-label="Search" />
                    <Button className="search-btn">
                      <i className="bi bi-search"></i>
                    </Button>
                  </Form>
                </Nav>
                <Nav className="ms-auto d-flex align-items-center">
                  <div className="d-flex align-items-center">
                    <div className="me-3 position-relative">
                      <i className="bi bi-bell"></i>
                      <Badge bg="danger" className="position-absolute top-0 start-100 translate-middle ">
                        2
                      </Badge>
                    </div>
                    <div className="me-3 position-relative">
                      <i className="bi bi-envelope"></i>
                      <Badge bg="success" className="position-absolute top-0 start-100 translate-middle ">
                        3
                      </Badge>
                    </div>
                    <Dropdown>
                      <Dropdown.Toggle variant="light" id="dropdown-basic">
                      <img 
          src={Avatar} 
          alt="Profile Avatar" 
          style={{ width: '35px', height: '35px', borderRadius: '50%' }} 
        />
                      </Dropdown.Toggle>
                      <Dropdown.Menu align="end">
                        <Dropdown.Item as={Link} to="/profile">Profile</Dropdown.Item>
                        <Dropdown.Item as={Link} to="/settings">Settings</Dropdown.Item>
                        <Dropdown.Divider />
                        <Dropdown.Item as={Link} to="/logout">Logout</Dropdown.Item>
                      </Dropdown.Menu>
                    </Dropdown>
                  </div>
                </Nav>
              </Navbar.Collapse>
            </Container>
          </Navbar>
        )}

        <div className="content">
          {children}
        </div>
      </div>
    </div>
  );
};

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

  const toggleSidebar = () => setSidebarCollapsed(!sidebarCollapsed);

  const handleLogin = (email, password) => {
  if (email === 'student@example.com' && password === 'password') {
    setIsAuthenticated(true);
    return true; // <-- Login success
  } else {
    alert('Invalid credentials');
    return false; // <-- Login failed
  }
};


  return (
    <Router>
      <AppLayout isAuthenticated={isAuthenticated} sidebarCollapsed={sidebarCollapsed} toggleSidebar={toggleSidebar}>
        <Routes>
          <Route path="/" element={isAuthenticated ? <Home /> : <Navigate to="/login" />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/login/student" element={<StudentLogin />} />
          <Route path="/login/teacher" element={<TeacherLogin />} />
          <Route path="/login/admin" element={<AdminLogin />} />
          <Route path="/login" element={<Login onLogin={handleLogin} />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </AppLayout>
    </Router>
  );
};

export default App;
