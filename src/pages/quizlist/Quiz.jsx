import React, { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import axios from 'axios';
import './Quiz.css'; // Custom CSS file

const QuizCard = () => {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/quizzes');
        setQuizzes(response.data);
      } catch (error) {
        console.error('Error fetching quiz data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="quiz-card-container">
      {quizzes.map((quiz, index) => (
        <div key={index} className="quiz-card">
          <div className="quiz-header">
            <span className="badge free">{quiz.status}</span>
            <span className="badge days-left">{quiz.daysLeft} Days Left</span>
          </div>
          <div className="quiz-content">
            <h3>{quiz.title}</h3>
            <p className="users-count">⚡ {quiz.users} Users</p>
            <ul className="quiz-details">
              <li>📝 {quiz.questions} Questions</li>
              <li>📄 {quiz.marks} Marks</li>
              <li>⏰ {quiz.time} Mins</li>
            </ul>
            <Button className="start-btn">Start Now</Button>
          </div>
          <div className="quiz-footer">
            <a href="#" className="syllabus-link">Syllabus</a>
            <span className="languages">📚 English, Hindi</span>
          </div>
        </div>
      ))}
    </div>
  );
};

export default QuizCard;
