import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { BookOpen, Brain, Target, Trophy } from 'lucide-react'

export default function PrepPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Exam Preparation</h1>

      <div className="grid md:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <Brain className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Mock Exams</CardTitle>
            <CardDescription>
              AI-generated practice tests for civil service exams
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Button>Start Practice Test</Button>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <BookOpen className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Study Materials</CardTitle>
            <CardDescription>
              Comprehensive guides and resources for government exams
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Button variant="outline">Browse Resources</Button>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <Target className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Interview Prep</CardTitle>
            <CardDescription>
              Common interview questions with STAR method examples
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Button variant="outline">Practice Interviews</Button>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <Trophy className="h-8 w-8 text-primary mb-2" />
            <CardTitle>Progress Tracking</CardTitle>
            <CardDescription>
              Monitor your preparation progress and identify weak areas
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Button variant="outline">View Analytics</Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
