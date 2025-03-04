import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CourseList from './components/CourseList';
import CourseDetails from './components/CourseDeatils'; // Corrected import
import AddCourse from './components/AddCourse';
import EditCourse from './components/EditCourse';
import StudentList from './components/StudentList';
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <h1>University Course Management</h1>
        <nav>
          <ul>
            <li><Link to="/courses">Courses</Link></li>
            <li><Link to="/students">Students</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/courses" element={<CourseList />} />
          <Route path="/courses/:courseId" element={<CourseDetails />} />
          <Route path="/courses/add" element={<AddCourse />} />
          <Route path="/courses/edit/:courseId" element={<EditCourse />} />
          <Route path="/students" element={<StudentList />} />
          <Route path="/" element={<CourseList />} />  {/* Default route */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
