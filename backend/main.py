from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager

from backend.core.config import settings
from backend.core.database import init_db
from backend.api import auth, jobs, applications, ai_tools, profile, prep, admin
from backend.services.ai_service import AIService


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    ai_service = AIService()
    await ai_service.load_models()
    app.state.ai_service = ai_service
    yield
    

app = FastAPI(
    title="GovLink API",
    version="1.0.0",
    description="AI-Powered Government Job Application Platform",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["Jobs"])
app.include_router(applications.router, prefix="/api/applications", tags=["Applications"])
app.include_router(ai_tools.router, prefix="/api/ai", tags=["AI Tools"])
app.include_router(profile.router, prefix="/api/profile", tags=["Profile"])
app.include_router(prep.router, prefix="/api/prep", tags=["Exam Prep"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])


@app.get("/")
async def root():
    return {
        "message": "GovLink API v1.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT
    }
