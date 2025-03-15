import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader

from app.core.config import settings

# Load Jinja2 templates
TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "../templates/emails")
print("~~~~~helo", TEMPLATES_PATH)
env = Environment(loader=FileSystemLoader("app/templates/emails"))

# SMTP Configuration from .env
SMTP_SERVER = settings.SMTP_HOST
SMTP_PORT = settings.SMTP_PORT
SMTP_USERNAME = settings.SMTP_USER
SMTP_PASSWORD = settings.SMTP_PASSWORD
SMTP_FROM = settings.SMTP_FROM_EMAIL


def render_email_template(template_name: str, context: dict) -> str:
    """Render an email template using Jinja2."""
    template = env.get_template(template_name)
    return template.render(context)


def send_email(to_email: str, subject: str, template_name: str, context: dict):
    """Send an email using SMTP."""
    # Render email content
    context["app_name"] = settings.APP_NAME  # Add app name to context
    html_content = render_email_template(template_name, context)

    # Construct email
    msg = MIMEMultipart()
    msg["From"] = SMTP_FROM
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(html_content, "html"))

    try:
        # Establish SMTP connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_FROM, to_email, msg.as_string())

        print(f"Email successfully sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")
