import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Briefcase, User, Search, BookOpen } from 'lucide-react'

export default function Navbar() {
  return (
    <nav className="border-b bg-card">
      <div className="container mx-auto px-4">
        <div className="flex h-16 items-center justify-between">
          <Link to="/" className="flex items-center space-x-2">
            <Briefcase className="h-6 w-6 text-primary" />
            <span className="text-xl font-bold">GovLink</span>
          </Link>
          
          <div className="flex items-center space-x-4">
            <Link to="/search">
              <Button variant="ghost" size="sm">
                <Search className="mr-2 h-4 w-4" />
                Search Jobs
              </Button>
            </Link>
            <Link to="/prep">
              <Button variant="ghost" size="sm">
                <BookOpen className="mr-2 h-4 w-4" />
                Exam Prep
              </Button>
            </Link>
            <Link to="/dashboard">
              <Button variant="ghost" size="sm">
                Dashboard
              </Button>
            </Link>
            <Link to="/login">
              <Button size="sm">
                <User className="mr-2 h-4 w-4" />
                Login
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}
