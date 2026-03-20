import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

const API_BASE = 'http://localhost:8000'

export default function PropertyDetailPage() {
  const { id } = useParams()
  const [property, setProperty] = useState(null)

  useEffect(() => {
    fetch(`${API_BASE}/properties/${id}`)
      .then((res) => res.json())
      .then(setProperty)
  }, [id])

  if (!property) return <main className="section">Loading…</main>

  return (
    <main className="section detail-layout">
      <img src={property.image_url} alt={property.title} className="detail-image" />
      <div>
        <h2>{property.title}</h2>
        <p>{property.description}</p>
        <p>{property.location}</p>
        <p>Bedrooms: {property.bedrooms} • Bathrooms: {property.bathrooms}</p>
        <p>Investment Score: {property.investment_score} • Rental Yield: {property.rental_yield}%</p>
        <h3>${property.price.toLocaleString()}</h3>
      </div>
    </main>
  )
}
