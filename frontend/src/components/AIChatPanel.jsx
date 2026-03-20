import { useState } from 'react'

const API_BASE = 'http://localhost:8000'

export default function AIChatPanel() {
  const [open, setOpen] = useState(false)
  const [input, setInput] = useState('Modern villas in Dubai under $3M')
  const [loading, setLoading] = useState(false)
  const [response, setResponse] = useState(null)

  const submit = async () => {
    setLoading(true)
    try {
      const res = await fetch(`${API_BASE}/ai/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input, session_id: 'ui-session' })
      })
      const data = await res.json()
      setResponse(data)
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <button className="ai-fab" onClick={() => setOpen(!open)}>AI</button>
      {open && (
        <aside className="ai-panel">
          <h4>Private Intelligence Agent</h4>
          <textarea value={input} onChange={(e) => setInput(e.target.value)} />
          <button className="btn btn-primary" onClick={submit}>Analyze</button>
          {loading && <p className="typing">Analyzing market signals…</p>}
          {response && (
            <div className="ai-response">
              <p>{response.message}</p>
              <div className="ai-cards">
                {response.properties.map((property) => (
                  <div key={property.id} className="mini-card">
                    <img src={property.image_url} alt={property.title} />
                    <div>
                      <h5>{property.title}</h5>
                      <p>{property.location}</p>
                    </div>
                  </div>
                ))}
              </div>
              <div className="suggestions">
                {response.suggestions.map((suggestion) => (
                  <button key={suggestion} className="btn btn-secondary">{suggestion}</button>
                ))}
              </div>
            </div>
          )}
        </aside>
      )}
    </>
  )
}
