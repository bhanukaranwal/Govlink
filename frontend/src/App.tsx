import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Toaster } from '@/components/ui/toaster'
import Navbar from '@/components/Navbar'
import HomePage from '@/pages/HomePage'
import SearchPage from '@/pages/SearchPage'
import DashboardPage from '@/pages/DashboardPage'
import ProfilePage from '@/pages/ProfilePage'
import PrepPage from '@/pages/PrepPage'
import LoginPage from '@/pages/LoginPage'
import RegisterPage from '@/pages/RegisterPage'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-background">
        <Navbar />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/search" element={<SearchPage />} />
            <Route path="/dashboard" element={<DashboardPage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="/prep" element={<PrepPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
          </Routes>
        </main>
        <Toaster />
      </div>
    </Router>
  )
}

export default App
