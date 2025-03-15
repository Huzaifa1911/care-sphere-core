from core.config import settings

from app.services.email.service import send_email
from app.workers.celery_app import celery


@celery.task(name="send_registration_email")
def send_registration_email(to_email: str, name: str):
    """Send a welcome email asynchronously."""
    send_email(
        to_email=to_email,
        subject=f"Welcome to {settings.APP_NAME}",
        template_name="welcome.html",
        context={"name": name},
    )
    return f"Welcome email sent to {to_email}"
