export default function Footer() {
  return (
    <footer className="footer">
      <div className="line" />
      <div className="footer-links">
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
        <a href="#">Contact</a>
      </div>
      <small>© {new Date().getFullYear()} MERIDIAN</small>
    </footer>
  )
}
