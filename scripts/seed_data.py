import asyncio
import sys
sys.path.append('.')

from backend.core.database import AsyncSessionLocal
from backend.models.job import Job
from backend.models.user import User
from backend.core.security import get_password_hash
from datetime import datetime, timedelta


async def seed_database():
    async with AsyncSessionLocal() as db:
        admin = User(
            email="[email protected]",
            hashed_password=get_password_hash("admin123"),
            full_name="Admin User",
            is_admin=True,
            is_verified=True
        )
        db.add(admin)
        
        sample_jobs = [
            Job(
                external_id="SAMPLE001",
                source="Sample",
                title="Data Analyst",
                organization="Department of Labor",
                description="Analyze employment data and create reports",
                location_city="Washington",
                location_state="DC",
                location_country="US",
                salary_min=65000,
                salary_max=85000,
                job_category="Data & Analytics",
                application_url="https://example.com/apply",
                posted_date=datetime.utcnow(),
                closing_date=datetime.utcnow() + timedelta(days=30),
                is_active=True
            ),
            Job(
                external_id="SAMPLE002",
                source="Sample",
                title="Program Manager",
                organization="Environmental Protection Agency",
                description="Manage environmental programs and initiatives",
                location_city="San Francisco",
                location_state="CA",
                location_country="US",
                salary_min=90000,
                salary_max=120000,
                job_category="Management",
                application_url="https://example.com/apply2",
                posted_date=datetime.utcnow(),
                closing_date=datetime.utcnow() + timedelta(days=45),
                is_active=True
            ),
            Job(
                external_id="SAMPLE003",
                source="Sample",
                title="Software Engineer",
                organization="Department of Technology",
                description="Develop and maintain government digital services",
                location_city="Austin",
                location_state="TX",
                location_country="US",
                salary_min=100000,
                salary_max=140000,
                job_category="Information Technology",
                remote_eligible=True,
                application_url="https://example.com/apply3",
                posted_date=datetime.utcnow(),
                closing_date=datetime.utcnow() + timedelta(days=60),
                is_active=True
            ),
        ]
        
        for job in sample_jobs:
            db.add(job)
        
        await db.commit()
        print("Database seeded successfully!")


if __name__ == "__main__":
    asyncio.run(seed_database())
