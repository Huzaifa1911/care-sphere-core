from celery import Celery

from app.core.config import settings

# Load settings from environment variables
REDIS_URL = settings.REDIS_URL

celery = Celery(
    settings.APP_NAME,
    broker=REDIS_URL,  # Message broker (Redis)
    backend=REDIS_URL,  # Result backend (Redis)
)

celery.conf.update(
    task_routes={
        "app.workers.tasks.*": {"queue": "default"},
    }
)
