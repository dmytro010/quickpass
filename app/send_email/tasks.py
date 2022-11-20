from proj.celery import app
from .service import send_weekly_news, send_secret

@app.task
def send_email_task(user_email, description, secret):
    send_secret(user_email, description, secret)

@app.task
def send_weekly_news_task():
    send_weekly_news()

@app.task
def hello():
    print("hello from celery task!")