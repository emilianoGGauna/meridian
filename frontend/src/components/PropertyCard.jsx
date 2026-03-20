import { Link } from 'react-router-dom'

export default function PropertyCard({ property }) {
  return (
    <article className="property-card">
      <img src={property.image_url} alt={property.title} />
      <div className="property-card-body">
        <h3>{property.title}</h3>
        <p>{property.location}</p>
        <strong>${property.price.toLocaleString()}</strong>
        <Link className="btn btn-primary" to={`/properties/${property.id}`}>View</Link>
      </div>
    </article>
  )
}
