import { useEffect, useState } from 'react'
import PropertyCard from '../components/PropertyCard'

const API_BASE = 'http://localhost:8000'

export default function ListingPage() {
  const [properties, setProperties] = useState([])

  useEffect(() => {
    fetch(`${API_BASE}/properties`)
      .then((res) => res.json())
      .then(setProperties)
  }, [])

  return (
    <main className="section">
      <h2>Global Portfolio</h2>
      <div className="property-grid">
        {properties.map((property) => <PropertyCard key={property.id} property={property} />)}
      </div>
    </main>
  )
}
