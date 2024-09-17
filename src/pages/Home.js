import React from 'react';
import { Card } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
const Home = () => {
  return (
    <Card>
      <Card.Body>
        <h1>Welcome to the Admin Panel Home</h1>
        <p>Manage your data efficiently through the admin panel.</p>
        <Button variant="primary" type='submit'>Primary</Button>{' '}
      </Card.Body>
    </Card>
  );
};

export default Home;
