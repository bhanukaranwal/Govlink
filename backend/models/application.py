from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, ForeignKey, Enum
from sqlalchemy.sql import func
from backend.core.database import Base
import enum


class ApplicationStatus(str, enum.Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    INTERVIEW = "interview"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"


class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False, index=True)
    
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.DRAFT, index=True)
    
    resume_text = Column(Text)
    cover_letter = Column(Text)
    ksc_responses = Column(JSON, default=[])
    
    ai_generated = Column(JSON, default={})
    form_data = Column(JSON, default={})
    documents = Column(JSON, default=[])
    
    submitted_at = Column(DateTime(timezone=True))
    last_updated = Column(DateTime(timezone=True))
    
    notes = Column(Text)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
