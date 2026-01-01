import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Sparkles, Target, BookOpen, Users, Globe, Zap } from 'lucide-react'

export default function HomePage() {
  return (
    <div className="space-y-16">
      <section className="text-center space-y-6 py-12">
        <h1 className="text-5xl font-bold tracking-tight">
          Find Your Dream Government Job
          <span className="block text-primary mt-2">Powered by AI</span>
        </h1>
        <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
          GovLink helps you discover, apply, and secure government positions worldwide
          with intelligent automation and personalized guidance.
        </p>
        <div className="flex gap-4 justify-center">
          <Link to="/search">
            <Button size="lg" className="text-lg px-8">
              Search Jobs
            </Button>
          </Link>
          <Link to="/register">
            <Button size="lg" variant="outline" className="text-lg px-8">
              Get Started Free
            </Button>
          </Link>
        </div>
      </section>

      <section className="grid md:grid-cols-3 gap-6">
        <Card>
          <CardHeader>
            <Sparkles className="h-8 w-8 text-primary mb-2" />
            <CardTitle>AI Resume Builder</CardTitle>
            <CardDescription>
              Generate tailored federal resumes and cover letters optimized for each position
            </CardDescription>
          </CardHeader>
        </Card>

        <Card>
          <CardHeader>
            <Target className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Smart Job Matching</CardTitle>
            <CardDescription>
              Get personalized job recommendations based on your skills and career goals
            </CardDescription>
          </CardHeader>
        </Card>

        <Card>
          <CardHeader>
            <BookOpen className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Exam Preparation</CardTitle>
            <CardDescription>
              AI-generated practice tests and study materials for civil service exams
            </CardDescription>
          </CardHeader>
        </Card>

        <Card>
          <CardHeader>
            <Users className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Community Support</CardTitle>
            <CardDescription>
              Connect with successful candidates and get mentorship from experts
            </CardDescription>
          </CardHeader>
        </Card>

        <Card>
          <CardHeader>
            <Globe className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Global Coverage</CardTitle>
            <CardDescription>
              Access government jobs from 25+ countries in 10+ languages
            </CardDescription>
          </CardHeader>
        </Card>

        <Card>
          <CardHeader>
            <Zap className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Application Automation</CardTitle>
            <CardDescription>
              Auto-fill complex forms and track all applications in one dashboard
            </CardDescription>
          </CardHeader>
        </Card>
      </section>

      <section className="bg-primary text-primary-foreground rounded-lg p-12 text-center">
        <h2 className="text-3xl font-bold mb-4">Join 500,000+ Job Seekers</h2>
        <p className="text-lg mb-6">
          Start your journey to a stable, rewarding government career today
        </p>
        <Link to="/register">
          <Button size="lg" variant="secondary">
            Create Free Account
          </Button>
        </Link>
      </section>
    </div>
  )
}
