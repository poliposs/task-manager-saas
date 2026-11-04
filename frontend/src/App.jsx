import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [healthStatus, setHealthStatus] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/health`)
      .then((response) => response.json())  
      .then((data) => setHealthStatus(data.status))
      .catch((err) => setError(err.message))
  }, [])

  return (
    <>
      <h1>Welcome to Task Manager</h1>
      {error ? (
        <p>Error: {error}</p>
      ) : healthStatus === null ? (
        <p>Checking backend…</p>
      ) : (
        <p>Backend status: {healthStatus}</p>
      )}
    </>
  )
}

export default App
