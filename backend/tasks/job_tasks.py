from backend.tasks.celery_app import celery_app
from backend.services.job_scraper import JobScraperService
from backend.core.database import AsyncSessionLocal
from backend.models.job import Job
from sqlalchemy import select


@celery_app.task
def scrape_jobs():
    import asyncio
    asyncio.run(_scrape_jobs_async())


async def _scrape_jobs_async():
    scraper = JobScraperService()
    jobs_data = await scraper.scrape_all_sources()
    
    async with AsyncSessionLocal() as db:
        for job_data in jobs_data:
            result = await db.execute(
                select(Job).where(Job.external_id == job_data['external_id'])
            )
            existing = result.scalar_one_or_none()
            
            if not existing:
                job = Job(**job_data)
                db.add(job)
        
        await db.commit()
    
    return len(jobs_data)


@celery_app.task
def update_job_status():
    import asyncio
    asyncio.run(_update_job_status_async())


async def _update_job_status_async():
    from datetime import datetime
    
    async with AsyncSessionLocal() as db:
        result = await db.execute(
            select(Job).where(Job.is_active == True)
        )
        jobs = result.scalars().all()
        
        updated = 0
        for job in jobs:
            if job.closing_date and job.closing_date < datetime.utcnow():
                job.is_active = False
                updated += 1
        
        await db.commit()
    
    return updated
