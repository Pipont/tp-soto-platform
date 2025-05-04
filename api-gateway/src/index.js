import express from 'express';
import dotenv from 'dotenv';
import { academicRoutes } from '../routes/academic.js';

dotenv.config();

const app = express();
app.use(express.json());

app.get('/health', (req, res) => {
  res.send({ status: 'API Gateway OK 🚀' });
});

// Middleware para rutas académicas
academicRoutes.forEach(({ path, proxy }) => {
  app.use(path, proxy);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`API Gateway corriendo en puerto ${PORT}`);
});
