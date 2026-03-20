import { useEffect, useState } from 'react'
import Hero from '../components/Hero'
import PropertyCard from '../components/PropertyCard'

const API_BASE = 'http://localhost:8000'

export default function HomePage() {
  const [properties, setProperties] = useState([])

  useEffect(() => {
    fetch(`${API_BASE}/properties`)
      .then((res) => res.json())
      .then((data) => setProperties(data.slice(0, 3)))
  }, [])

  return (
    <main>
      <Hero />
      <section className="section">
        <h2>Curated Signatures</h2>
        <div className="property-grid">
          {properties.map((property) => <PropertyCard key={property.id} property={property} />)}
        </div>
      </section>
      <section className="section insta-grid">
        <div className="tile logo">MERIDIAN</div>
        <div className="tile texture" />
        <div className="tile architecture" />
        <div className="tile logo">AXIS</div>
      </section>
    </main>
  )
}
