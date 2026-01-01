import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Search, MapPin, Building, DollarSign } from 'lucide-react'
import axios from 'axios'

export default function SearchPage() {
  const [keyword, setKeyword] = useState('')
  const [location, setLocation] = useState('')

  const { data: jobs, isLoading } = useQuery({
    queryKey: ['jobs', keyword, location],
    queryFn: async () => {
      const response = await axios.get('/api/jobs/search', {
        params: { keyword, location, page: 1, limit: 20 }
      })
      return response.data
    },
  })

  return (
    <div className="space-y-6">
      <div className="bg-card p-6 rounded-lg border">
        <h1 className="text-3xl font-bold mb-6">Search Government Jobs</h1>
        <div className="flex gap-4">
          <div className="flex-1">
            <Input
              placeholder="Job title, keywords, or company"
              value={keyword}
              onChange={(e) => setKeyword(e.target.value)}
              className="w-full"
            />
          </div>
          <div className="flex-1">
            <Input
              placeholder="City, state, or zip code"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              className="w-full"
            />
          </div>
          <Button>
            <Search className="mr-2 h-4 w-4" />
            Search
          </Button>
        </div>
      </div>

      <div className="space-y-4">
        {isLoading && <p>Loading jobs...</p>}
        
        {jobs && jobs.length === 0 && (
          <Card>
            <CardContent className="py-12 text-center">
              <p className="text-muted-foreground">No jobs found. Try different keywords.</p>
            </CardContent>
          </Card>
        )}

        {jobs?.map((job: any) => (
          <Card key={job.id} className="hover:shadow-md transition-shadow">
            <CardHeader>
              <CardTitle>{job.title}</CardTitle>
              <CardDescription>
                <div className="flex flex-wrap gap-4 mt-2">
                  <span className="flex items-center">
                    <Building className="mr-1 h-4 w-4" />
                    {job.organization}
                  </span>
                  <span className="flex items-center">
                    <MapPin className="mr-1 h-4 w-4" />
                    {job.location_city}, {job.location_state}
                  </span>
                  {job.salary_min && (
                    <span className="flex items-center">
                      <DollarSign className="mr-1 h-4 w-4" />
                      ${job.salary_min.toLocaleString()} - ${job.salary_max?.toLocaleString()}
                    </span>
                  )}
                </div>
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground line-clamp-2 mb-4">
                {job.description}
              </p>
              <Button>View Details</Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}
