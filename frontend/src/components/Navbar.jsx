import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="logo-wordmark">MERIDIAN</div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/properties">Properties</Link>
        <Link to="/insights">Insights</Link>
      </nav>
    </header>
  )
}
