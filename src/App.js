import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { Navbar, Nav, Button, Container, Dropdown, Badge, Form } from 'react-bootstrap';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import StudentLogin from './pages/Login/StudentLogin';
import TeacherLogin from './pages/Login/TeacherLogin';
import AdminLogin from './pages/Login/AdminLogin';
import './App.css';
import Logo from './Assets/imgs/logo.jpg'; // Website logo
import Favicon from './Assets/imgs/favicon.jpg'; // Favicon image

const App = () => {
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
  const [loginDropdownOpen, setLoginDropdownOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarCollapsed(!sidebarCollapsed);
  };

  const toggleLoginDropdown = () => {
    setLoginDropdownOpen(!loginDropdownOpen);
  };

  return (
    <Router>
      <div className="d-flex">
        {/* Sidebar */}
        <nav className={`bg-dark text-white p-3 sidebar ${sidebarCollapsed ? 'collapsed' : ''}`}>
          {/* Logo Section */}
          <div className="logo-section text-center mb-3">
            <Link to="/" onClick={() => setSidebarCollapsed(false)}>
              {!sidebarCollapsed ? (
                <img
                  src={Logo}
                  alt="Logo"
                  className="logo-img"
                  style={{ maxWidth: '100%', height: '50px', transition: 'all 0.3s ease' }}
                />
              ) : (
                <img
                  src={Favicon}
                  alt="Favicon"
                  className="favicon-img"
                  style={{ maxWidth: '50px', height: '50px', transition: 'all 0.3s ease' }}
                />
              )}
            </Link>
          </div>

          <ul className="nav flex-column">
            <li className="nav-item">
              <Link to="/" className="nav-link text-white" onClick={() => setSidebarCollapsed(false)}>
                <i className="bi bi-house" id="dash-icon"></i>  {!sidebarCollapsed && ' Dashboard'}
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/about" className="nav-link text-white" onClick={() => setSidebarCollapsed(false)}>
                <i className="bi bi-info-circle" id="dash-icon"></i>  {!sidebarCollapsed && ' About'}
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/contact" className="nav-link text-white" onClick={() => setSidebarCollapsed(false)}>
                <i className="bi bi-envelope" id="dash-icon"></i> {!sidebarCollapsed && ' Contact'}
              </Link>
            </li>

            {/* Dropdown for Login */}
            <li className="nav-item">
              <div className="nav-link text-white" onClick={toggleLoginDropdown} style={{ cursor: 'pointer' }}>
                <i className="bi bi-key" id="icon"></i> {!sidebarCollapsed && ' Login'}
                <i className={`bi ${loginDropdownOpen ? 'bi-caret-up-fill' : 'bi-caret-down-fill'}`}></i>
              </div>
              {loginDropdownOpen && (
                <ul className="nav flex-column ms-3">
                  <li className="nav-item">
                    <Link to="/login/student" className="nav-link text-white" onClick={() => setLoginDropdownOpen(false)}>
                      Student Login
                    </Link>
                  </li>
                  <li className="nav-item">
                    <Link to="/login/teacher" className="nav-link text-white" onClick={() => setLoginDropdownOpen(false)}>
                      Teacher Login
                    </Link>
                  </li>
                  <li className="nav-item">
                    <Link to="/login/admin" className="nav-link text-white" onClick={() => setLoginDropdownOpen(false)}>
                      Admin Login
                    </Link>
                  </li>
                </ul>
              )}
            </li>
          </ul>
        </nav>

        {/* Main content area */}
        <div className="w-100">
          <Navbar bg="light" expand="lg" className="mb-4 nav-clr">
            <Container>
              {/* Toggle button */}
              <Button variant="outline-secondary" onClick={toggleSidebar} className="me-3" id="toggle-icon">
                <i className="bi bi-list"></i>
              </Button>
              <Navbar.Brand className="logo d-lg-none"> {/* Show only on mobile */}
                <img src={Logo} alt="Logo" style={{ height: '40px' }} />
              </Navbar.Brand>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                  {/* Search Bar */}
                  <Form className="d-flex">
                    <Form.Control
                      type="search"
                      placeholder="Search..."
                      className="me-2"
                      aria-label="Search"
                    />
                    <Button variant="outline-success">
                      <i className="bi bi-search"></i>
                    </Button>
                  </Form>
                </Nav>
                <Nav className="ms-auto d-flex align-items-center">
                  <div className="noti-prof d-flex align-items-center">
                    {/* First Notification */}
                    <div className="notify me-3 position-relative">
                      <i className="bi bi-bell"></i>
                      <Badge bg="danger" className="position-absolute top-0 start-100 translate-middle p-2">
                        2
                      </Badge>
                    </div>
                    {/* Second Notification */}
                    <div className="notify me-3 position-relative">
                      <i className="bi bi-envelope"></i>
                      <Badge bg="success" className="position-absolute top-0 start-100 translate-middle p-2">
                        3
                      </Badge>
                    </div>
                    {/* Profile Dropdown */}
                    <Dropdown>
                      <Dropdown.Toggle variant="light" id="dropdown-basic" className="profile-toggle">
                        <i className="bi bi-person-circle"></i>
                      </Dropdown.Toggle>

                      <Dropdown.Menu align="end"> {/* Aligns the dropdown to the right */}
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

          <Container>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/contact" element={<Contact />} />
              {/* Routes for login sections */}
              <Route path="/login/student" element={<StudentLogin />} />
              <Route path="/login/teacher" element={<TeacherLogin />} />
              <Route path="/login/admin" element={<AdminLogin />} />
            </Routes>
          </Container>
        </div>
      </div>
    </Router>
  );
};

export default App;
