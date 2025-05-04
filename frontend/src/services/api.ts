import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Asegúrate de que esto coincida con academic-management
});

export default api;
