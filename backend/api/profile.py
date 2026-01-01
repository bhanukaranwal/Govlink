from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.user import User
from backend.schemas.user import UserProfile, UserResponse

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_profile(
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalar_one_or_none()
    return UserResponse.from_orm(user)


@router.put("/me")
async def update_profile(
    profile_data: UserProfile,
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalar_one_or_none()
    
    user.profile_data = profile_data.dict()
    user.skills = profile_data.skills
    user.preferences = profile_data.preferences
    
    await db.commit()
    return {"message": "Profile updated successfully"}
