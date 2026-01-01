# GovLink Setup Guide

## Prerequisites

- Docker 24+ and Docker Compose
- 8GB RAM minimum
- 20GB disk space
- (Optional) USAJOBS API key from https://developer.usajobs.gov

## Quick Start

1. Clone repository:
    bash
git clone https://github.com/yourusername/govlink.git
cd govlink

Configure environment:

cp .env.example .env

Edit .env and add your API keys (optional for demo).

Start services:

docker-compose up -d
Wait for initialization (5-10 minutes):

PostgreSQL database setup

AI model download (Mistral-7B ~4GB)

Sample data seeding

Access platform:

Frontend: http://localhost:3000

API: http://localhost:8000

API Docs: http://localhost:8000/docs

Celery Monitor: http://localhost:5555

Initial Login
Default admin account:

Email: [email protected]

Password: admin123

Change password after first login!

Seeding Data
docker-compose exec backend python scripts/seed_data.py
Running Scraper Manually
docker-compose exec backend python scripts/run_scraper.py
Development Mode
Backend:
cd backend
python -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
uvicorn main:app --reload
Frontend:

cd frontend
npm install
npm run dev
Troubleshooting
Models not downloading:

Check internet connection

Increase Docker memory limit to 8GB

Manually download from HuggingFace

Database connection errors:

Ensure PostgreSQL is healthy: docker-compose ps

Check logs: docker-compose logs postgres

Frontend not loading:

Clear browser cache

Check backend is running: curl http://localhost:8000/health

Production Deployment
See docs/deployment.md for Kubernetes setup and production best practices.
Support
GitHub Issues: https://github.com/yourusername/govlink/issues
