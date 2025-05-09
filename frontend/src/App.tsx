import { useState } from 'react'
import './App.css'
import StudentForm from './components/StudentForm';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <StudentForm />
    </div>
  );
}

export default App;
