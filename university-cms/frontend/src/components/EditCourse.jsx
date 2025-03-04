import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import api from '../services/api';

function EditCourse() {
  const { courseId } = useParams();
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [credits, setCredits] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchCourse() {
      try {
        const response = await api.get(`/courses/${courseId}`);
        const course = response.data;
        setName(course.name);
        setDescription(course.description);
        setCredits(course.credits);
      } catch (error) {
        console.error('Error fetching course:', error);
        navigate('/courses'); // Redirect if course not found
      }
    }

    fetchCourse();
  }, [courseId, navigate]);

  async function handleSubmit(event) {
    event.preventDefault();

    try {
      await api.put(`/courses/${courseId}`, { name, description, credits });
      navigate(`/courses/${courseId}`); // Redirect to course details
    } catch (error) {
      console.error('Error updating course:', error);
      alert('Failed to update course');
    }
  }

  return (
    <div>
      <h2>Edit Course</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="credits">Credits:</label>
          <input
            type="number"
            id="credits"
            value={credits}
            onChange={(e) => setCredits(e.target.value)}
          />
        </div>
        <button type="submit">Update Course</button>
        <Link to={`/courses/${courseId}`}>Cancel</Link>
      </form>
    </div>
  );
}

export default EditCourse;
