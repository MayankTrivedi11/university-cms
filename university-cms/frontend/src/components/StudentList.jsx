import React, { useState, useEffect } from 'react';
import api from '../services/api';

function StudentList() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    async function fetchStudents() {
      try {
        const response = await api.get('/students');
        setStudents(response.data);
      } catch (error) {
        console.error('Error fetching students:', error);
      }
    }

    fetchStudents();
  }, []);

  return (
    <div>
      <h2>Student List</h2>
      <ul>
        {students.map(student => (
          <li key={student.id}>
            {student.name} ({student.email}) - {student.major}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StudentList;
