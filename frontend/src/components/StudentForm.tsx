import { useState } from 'react';
import api from '../services/api';

export default function StudentForm() {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    gender: '',
    grade: '',
    school_id: ''
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await api.post('/students/', {
        ...formData,
        age: parseInt(formData.age),
        school_id: parseInt(formData.school_id),
      });
      alert("✅ Estudiante creado: " + response.data.name);
    } catch (error) {
      console.error("❌ Error al registrar estudiante", error);
      alert("Ocurrió un error al registrar el estudiante");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto bg-white p-6 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Registrar Estudiante</h2>

      <label className="block mb-2">
        Nombre:
        <input type="text" name="name" value={formData.name} onChange={handleChange} className="mt-1 block w-full border rounded p-2" />
      </label>

      <label className="block mb-2">
        Edad:
        <input type="number" name="age" value={formData.age} onChange={handleChange} className="mt-1 block w-full border rounded p-2" />
      </label>

      <label className="block mb-2">
        Género:
        <select name="gender" value={formData.gender} onChange={handleChange} className="mt-1 block w-full border rounded p-2">
          <option value="">Seleccione</option>
          <option value="1">Masculino</option>
          <option value="0">Femenino</option>
        </select>
      </label>

      <label className="block mb-2">
        Grado:
        <input type="text" name="grade" value={formData.grade} onChange={handleChange} className="mt-1 block w-full border rounded p-2" />
      </label>

      <label className="block mb-4">
        ID del Colegio:
        <input type="number" name="school_id" value={formData.school_id} onChange={handleChange} className="mt-1 block w-full border rounded p-2" />
      </label>

      <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Registrar</button>
    </form>
  );
}
