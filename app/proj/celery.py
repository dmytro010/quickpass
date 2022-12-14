import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj', broker='redis://redis:6379')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    # Executes every Monday morning at 9:30 a.m. crontab(hour=9, minute=30, day_of_week=1)
    'send-weekly-news-every-monday': {
        'task': 'send_email.tasks.send_weekly_news_task',
        'schedule': crontab(hour=9, minute=30, day_of_week=1),
    },
}

