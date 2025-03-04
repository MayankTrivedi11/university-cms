import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';

function CourseList() {
  const [courses, setCourses] = useState([]);
  const [selectedCourseId, setSelectedCourseId] = useState(null); // State to track the selected course

  useEffect(() => {
    async function fetchCourses() {
      try {
        const response = await api.get('/courses');
        setCourses(response.data);
      } catch (error) {
        console.error('Error fetching courses:', error);
        // If API fails to load, use the default courses
        setCourses(defaultCourses);
      }
    }

    fetchCourses();
  }, []);

  // Default courses to display if the API fails
  const defaultCourses = [
    { id: '1', name: 'Introduction to React', description: 'Learn the basics of React', credits: 3 },
    { id: '2', name: 'Advanced JavaScript', description: 'Deep dive into JavaScript concepts', credits: 4 },
    { id: '3', name: 'Python for Data Science', description: 'Using Python for data analysis', credits: 3 },
  ];

  const handleCourseClick = (courseId) => {
    setSelectedCourseId(courseId === selectedCourseId ? null : courseId); // Toggle selection
  };

  return (
    <div>
      <h2>Course List</h2>
      <ul>
        {courses.length > 0 ? (
          courses.map(course => (
            <li key={course.id}>
              <Link to={`/courses/${course.id}`} onClick={(e) => {
                  e.preventDefault(); // Prevent default link behavior
                  handleCourseClick(course.id);
                }}>
                  {course.name}
              </Link>
              {selectedCourseId === course.id && (
                <p>{course.description}</p>
              )}
            </li>
          ))
        ) : (
          <li>No courses found.</li>
        )}
      </ul>
      <Link to="/courses/add">Add New Course</Link>
    </div>
  );
}

export default CourseList;
