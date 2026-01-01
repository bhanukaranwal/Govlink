from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.application import Application
from backend.schemas.application import ApplicationCreate, ApplicationResponse, ApplicationDetail

router = APIRouter()


@router.post("/", response_model=ApplicationResponse)
async def create_application(
    app_data: ApplicationCreate,
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    application = Application(
        user_id=int(user_id),
        job_id=app_data.job_id,
        resume_text=app_data.resume_text,
        cover_letter=app_data.cover_letter,
        form_data=app_data.form_data
    )
    db.add(application)
    await db.commit()
    await db.refresh(application)
    
    return ApplicationResponse.from_orm(application)


@router.get("/", response_model=List[ApplicationResponse])
async def get_my_applications(
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Application).where(Application.user_id == int(user_id))
    )
    applications = result.scalars().all()
    
    return [ApplicationResponse.from_orm(app) for app in applications]


@router.get("/{application_id}", response_model=ApplicationDetail)
async def get_application(
    application_id: int,
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Application).where(
            Application.id == application_id,
            Application.user_id == int(user_id)
        )
    )
    application = result.scalar_one_or_none()
    
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    return ApplicationDetail.from_orm(application)
