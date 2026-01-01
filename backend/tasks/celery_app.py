from celery import Celery
from celery.schedules import crontab
from backend.core.config import settings

celery_app = Celery(
    'govlink',
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    beat_schedule={
        'scrape-jobs-daily': {
            'task': 'backend.tasks.job_tasks.scrape_jobs',
            'schedule': crontab(hour=2, minute=0),
        },
        'update-job-status': {
            'task': 'backend.tasks.job_tasks.update_job_status',
            'schedule': crontab(hour='*/6'),
        },
    }
)
