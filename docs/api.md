# GovLink API Documentation

Base URL: `http://localhost:8000/api`

## Authentication

### Register
`POST /auth/register`

Request:
   json
{
  "email": "[email protected]",
  "password": "secure123",
  "full_name": "John Doe"
}

Login
POST /auth/login

Returns JWT token for authenticated requests.

Jobs
Search Jobs
GET /jobs/search?keyword=analyst&location=DC&page=1&limit=20

Get Job Details
GET /jobs/{job_id}

Get Recommendations
GET /jobs/recommendations/

Requires authentication.

Applications
Create Application
POST /applications/

Get My Applications
GET /applications/

Get Application Details
GET /applications/{application_id}

AI Tools
Generate Resume
POST /ai/generate-resume

Generate Cover Letter
POST /ai/generate-cover-letter

Skill Match Analysis
POST /ai/skill-match?job_id={id}

Exam Prep
Generate Mock Exam
POST /prep/generate-exam

Get Interview Questions
GET /prep/interview-questions/{category}

Rate Limits
100 requests per minute per IP

1000 requests per hour per authenticated user

Error Responses
{
  "detail": "Error message"
}
