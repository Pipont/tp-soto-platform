import { createProxyMiddleware } from 'http-proxy-middleware';

const academicServiceUrl = process.env.ACADEMIC_MANAGEMENT_URL || 'http://academic-management:8000';

export const academicRoutes = [
  {
    path: '/students',
    proxy: createProxyMiddleware({
      target: academicServiceUrl,
      changeOrigin: true,
      pathRewrite: { '^/students': '/students' }
    })
  },
  {
    path: '/student-surveys',
    proxy: createProxyMiddleware({
      target: academicServiceUrl,
      changeOrigin: true,
      pathRewrite: { '^/student-surveys': '/student-surveys' }
    })
  },
  {
    path: '/teachers',
    proxy: createProxyMiddleware({
      target: academicServiceUrl,
      changeOrigin: true,
      pathRewrite: { '^/teachers': '/teachers' }
    })
  },
  {
    path: '/schools',
    proxy: createProxyMiddleware({
      target: academicServiceUrl,
      changeOrigin: true,
      pathRewrite: { '^/schools': '/schools' }
    })
  },
  {
    path: '/courses',
    proxy: createProxyMiddleware({
      target: academicServiceUrl,
      changeOrigin: true,
      pathRewrite: { '^/courses': '/courses' }
    })
  },
  {
    path: '/math-assessments',
    proxy: createProxyMiddleware({
      target: academicServiceUrl,
      changeOrigin: true,
      pathRewrite: { '^/math-assessments': '/math-assessments' }
    })
  }
];
