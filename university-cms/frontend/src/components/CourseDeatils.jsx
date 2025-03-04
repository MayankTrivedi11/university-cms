import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import api from '../services/api';

function CourseDetails() {
  const { courseId } = useParams();
  const [course, setCourse] = useState(null);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true); // Add loading state
  const [error, setError] = useState(null);     // Add error state

  useEffect(() => {
    const fetchCourse = async () => {
      setLoading(true);
      setError(null); // Reset error on each fetch

      try {
        const response = await api.get(`/courses/${courseId}`);
        setCourse(response.data);
      } catch (err) {
        console.error('Error fetching course:', err);
        setError(err.message || 'Failed to fetch course'); // Set error message
        // Optionally, redirect to a "not found" page after a delay
        // setTimeout(() => navigate('/courses'), 3000);
      } finally {
        setLoading(false);
      }
    };

    fetchCourse();
  }, [courseId, navigate]);

  const handleDelete = async () => {
    try {
      await api.delete(`/courses/${courseId}`);
      navigate('/courses'); // Redirect back to course list
    } catch (err) {
      console.error('Error deleting course:', err);
      alert('Failed to delete course: ' + (err.message || 'Unknown error'));
    }
  };

  if (loading) {
    return <div>Loading course details...</div>; // Show loading indicator
  }

  if (error) {
    return (
      <div>
        Error: {error}
        <Link to="/courses">Back to Course List</Link>
      </div>
    ); // Show error message
  }

  if (!course) {
    return <div>Course not found.</div>; // Show "not found" message
  }

  return (
    <div>
      <h2>{course.name}</h2>
      <p>{course.description}</p>
      <p>Credits: {course.credits}</p>
      <Link to={`/courses/edit/${courseId}`}>Edit</Link> |
      <button onClick={handleDelete}>Delete</button> |
      <Link to="/courses">Back to List</Link>
    </div>
  );
}

export default CourseDetails;
