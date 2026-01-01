from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_
from typing import List

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.job import Job
from backend.schemas.job import JobResponse, JobDetail, JobSearch

router = APIRouter()


@router.get("/search", response_model=List[JobResponse])
async def search_jobs(
    keyword: str = Query(None),
    location: str = Query(None),
    category: str = Query(None),
    remote_only: bool = False,
    page: int = 1,
    limit: int = 20,
    db: AsyncSession = Depends(get_db)
):
    query = select(Job).where(Job.is_active == True)
    
    if keyword:
        query = query.where(
            or_(
                Job.title.ilike(f"%{keyword}%"),
                Job.description.ilike(f"%{keyword}%")
            )
        )
    
    if location:
        query = query.where(
            or_(
                Job.location_city.ilike(f"%{location}%"),
                Job.location_state.ilike(f"%{location}%")
            )
        )
    
    if category:
        query = query.where(Job.job_category == category)
    
    if remote_only:
        query = query.where(Job.remote_eligible == True)
    
    query = query.offset((page - 1) * limit).limit(limit)
    result = await db.execute(query)
    jobs = result.scalars().all()
    
    return [JobResponse.from_orm(job) for job in jobs]


@router.get("/{job_id}", response_model=JobDetail)
async def get_job(job_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return JobDetail.from_orm(job)


@router.get("/recommendations/", response_model=List[JobResponse])
async def get_recommendations(
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    query = select(Job).where(Job.is_active == True).limit(10)
    result = await db.execute(query)
    jobs = result.scalars().all()
    
    return [JobResponse.from_orm(job) for job in jobs]
