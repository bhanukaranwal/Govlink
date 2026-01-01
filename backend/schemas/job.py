from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime


class JobBase(BaseModel):
    title: str
    organization: str
    description: str
    location_city: Optional[str]
    location_state: Optional[str]
    location_country: str = "US"


class JobCreate(JobBase):
    external_id: str
    source: str
    qualifications: Optional[str]
    responsibilities: Optional[str]
    salary_min: Optional[float]
    salary_max: Optional[float]
    job_category: Optional[str]
    application_url: str
    posted_date: datetime
    closing_date: Optional[datetime]


class JobSearch(BaseModel):
    keyword: Optional[str]
    location: Optional[str]
    category: Optional[str]
    salary_min: Optional[float]
    remote_only: bool = False
    page: int = 1
    limit: int = 20


class JobResponse(JobBase):
    id: int
    external_id: str
    source: str
    salary_min: Optional[float]
    salary_max: Optional[float]
    job_category: Optional[str]
    closing_date: Optional[datetime]
    application_url: str
    match_score: Optional[float] = None
    
    class Config:
        from_attributes = True


class JobDetail(JobResponse):
    qualifications: Optional[str]
    responsibilities: Optional[str]
    requirements: List[str] = []
    keywords: List[str] = []
