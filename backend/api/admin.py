from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.database import get_db
from backend.core.security import get_current_user

router = APIRouter()


@router.get("/stats")
async def get_platform_stats(
    user_id: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return {
        "total_jobs": 0,
        "total_applications": 0,
        "total_users": 0,
        "success_rate": 0.0
    }
