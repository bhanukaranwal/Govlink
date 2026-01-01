from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, Float, Boolean
from sqlalchemy.sql import func
from backend.core.database import Base


class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, unique=True, index=True)
    source = Column(String, index=True)
    
    title = Column(String, nullable=False, index=True)
    organization = Column(String, index=True)
    department = Column(String)
    
    description = Column(Text)
    qualifications = Column(Text)
    responsibilities = Column(Text)
    
    location_city = Column(String, index=True)
    location_state = Column(String, index=True)
    location_country = Column(String, index=True, default="US")
    remote_eligible = Column(Boolean, default=False)
    
    salary_min = Column(Float)
    salary_max = Column(Float)
    salary_currency = Column(String, default="USD")
    
    job_category = Column(String, index=True)
    job_level = Column(String)
    employment_type = Column(String)
    
    posted_date = Column(DateTime(timezone=True))
    closing_date = Column(DateTime(timezone=True), index=True)
    
    application_url = Column(String)
    requirements = Column(JSON, default=[])
    keywords = Column(JSON, default=[])
    
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
