import React, { useEffect, useState } from 'react';
import { Table, Button, Spinner, Container } from 'react-bootstrap';
import axios from 'axios';
import './QuizList.css'; // Custom CSS file

const QuizList = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from the API
    const fetchData = async () => {
      try {
        const response = await axios.get('https://api.example.com/quiz-list');
        setQuizzes(response.data);
      } catch (error) {
        console.error('Error fetching quiz data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="spinner-container">
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    );
  }

  return (
    <Container className="quiz-list-container">
      <h2 className="text-center mb-4">Quiz Items</h2>
      <Table striped bordered hover responsive className="quiz-list-table">
        <thead className="table-header">
          <tr>
            <th>Status</th>
            <th>Days Left</th>
            <th>Title</th>
            <th>Users</th>
            <th>Questions</th>
            <th>Marks</th>
            <th>Time</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {quizzes.map((quiz, index) => (
            <tr key={index}>
              <td>{quiz.status}</td>
              <td>{quiz.daysLeft}</td>
              <td>{quiz.title}</td>
              <td>{quiz.users}</td>
              <td>{quiz.questions}</td>
              <td>{quiz.marks}</td>
              <td>{quiz.time}</td>
              <td>
                <Button variant="success" size="sm" className="me-2">
                  {quiz.actions.start}
                </Button>
                <Button variant="info" size="sm">
                  {quiz.actions.syllabus}
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default QuizList;
