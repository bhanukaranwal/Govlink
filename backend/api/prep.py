from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from typing import List

from backend.core.security import get_current_user

router = APIRouter()


class ExamRequest(BaseModel):
    exam_type: str
    topic: str
    difficulty: str = "medium"
    num_questions: int = 10


@router.post("/generate-exam")
async def generate_mock_exam(
    request: ExamRequest,
    app: Request,
    user_id: str = Depends(get_current_user)
):
    ai_service = app.app.state.ai_service
    questions = await ai_service.generate_exam_questions(
        request.exam_type,
        request.topic,
        request.difficulty,
        request.num_questions
    )
    return {"questions": questions}


@router.get("/interview-questions/{job_category}")
async def get_interview_questions(
    job_category: str,
    app: Request,
    user_id: str = Depends(get_current_user)
):
    ai_service = app.app.state.ai_service
    questions = await ai_service.generate_interview_questions(job_category)
    return {"questions": questions}
