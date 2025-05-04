import fetch from 'node-fetch'
export async function proxyRequest(req, res, targetUrl) {
  try {
    const response = await fetch(targetUrl, {
      method: req.method,
      headers: { 'Content-Type': 'application/json' },
      body: ['GET', 'DELETE'].includes(req.method) ? null : JSON.stringify(req.body),
    })

    const data = await response.json()
    res.status(response.status).json(data)
  } catch (error) {
    console.error('❌ Error en proxy:', error.message)
    res.status(500).json({ error: 'Error interno en API Gateway' })
  }
}
