# routes/dashboard.py
from flask import Blueprint, session, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    username = session.get('username')
    role = session.get('role')
    if not username:
        return redirect(url_for('auth.login'))

    if role == "admin":
        return f"Admin Dashboard for {username}"
    else:
        return f"User Dashboard for {username}"
