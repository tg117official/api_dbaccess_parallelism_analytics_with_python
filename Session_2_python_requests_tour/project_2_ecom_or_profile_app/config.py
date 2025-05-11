# config.py
from datetime import timedelta

SECRET_KEY = 'supersecretkey'
PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)  # Auto-expire session after 5 minutes
