import asyncio
import sys
sys.path.append('.')

from backend.services.job_scraper import JobScraperService
from backend.core.database import AsyncSessionLocal
from backend.models.job import Job
from sqlalchemy import select


async def main():
    scraper = JobScraperService()
    print("Starting job scraping...")
    
    jobs_data = await scraper.scrape_all_sources()
    print(f"Found {len(jobs_data)} jobs")
    
    async with AsyncSessionLocal() as db:
        for job_data in jobs_data:
            result = await db.execute(
                select(Job).where(Job.external_id == job_data['external_id'])
            )
            existing = result.scalar_one_or_none()
            
            if not existing:
                job = Job(**job_data)
                db.add(job)
                print(f"Added: {job_data['title']}")
        
        await db.commit()
    
    print("Scraping complete!")


if __name__ == "__main__":
    asyncio.run(main())
