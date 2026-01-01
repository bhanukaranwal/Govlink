from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from typing import List, Dict

from backend.core.security import get_current_user

router = APIRouter()


class ResumeRequest(BaseModel):
    job_description: str
    user_profile: Dict
    format_type: str = "federal"


class CoverLetterRequest(BaseModel):
    job_description: str
    user_profile: Dict
    company_name: str


@router.post("/generate-resume")
async def generate_resume(
    request: ResumeRequest,
    app: Request,
    user_id: str = Depends(get_current_user)
):
    ai_service = app.app.state.ai_service
    resume = await ai_service.generate_resume(
        request.job_description,
        request.user_profile,
        request.format_type
    )
    return {"resume": resume}


@router.post("/generate-cover-letter")
async def generate_cover_letter(
    request: CoverLetterRequest,
    app: Request,
    user_id: str = Depends(get_current_user)
):
    ai_service = app.app.state.ai_service
    cover_letter = await ai_service.generate_cover_letter(
        request.job_description,
        request.user_profile,
        request.company_name
    )
    return {"cover_letter": cover_letter}


@router.post("/skill-match")
async def analyze_skill_match(
    job_id: int,
    app: Request,
    user_id: str = Depends(get_current_user)
):
    ai_service = app.app.state.ai_service
    analysis = await ai_service.analyze_skill_match(user_id, job_id)
    return analysis
