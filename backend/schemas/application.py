from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime
from backend.models.application import ApplicationStatus


class ApplicationCreate(BaseModel):
    job_id: int
    resume_text: Optional[str]
    cover_letter: Optional[str]
    form_data: Dict = {}


class ApplicationUpdate(BaseModel):
    status: Optional[ApplicationStatus]
    resume_text: Optional[str]
    cover_letter: Optional[str]
    ksc_responses: Optional[List[Dict]]
    notes: Optional[str]


class ApplicationResponse(BaseModel):
    id: int
    job_id: int
    status: ApplicationStatus
    submitted_at: Optional[datetime]
    created_at: datetime
    
    class Config:
        from_attributes = True


class ApplicationDetail(ApplicationResponse):
    resume_text: Optional[str]
    cover_letter: Optional[str]
    ksc_responses: List[Dict] = []
    ai_generated: Dict = {}
    notes: Optional[str]
