import { Route, Routes } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import AIChatPanel from './components/AIChatPanel'
import HomePage from './pages/HomePage'
import ListingPage from './pages/ListingPage'
import PropertyDetailPage from './pages/PropertyDetailPage'
import InsightsPage from './pages/InsightsPage'

export default function App() {
  return (
    <div className="app-shell">
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/properties" element={<ListingPage />} />
        <Route path="/properties/:id" element={<PropertyDetailPage />} />
        <Route path="/insights" element={<InsightsPage />} />
      </Routes>
      <Footer />
      <AIChatPanel />
    </div>
  )
}
