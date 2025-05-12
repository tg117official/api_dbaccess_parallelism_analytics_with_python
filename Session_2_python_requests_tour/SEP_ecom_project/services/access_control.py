# utils/access_control.py
from functools import wraps
from flask import session, redirect, url_for, abort

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            username = session.get('username')
            user_role = session.get('role')

            if not username:
                return redirect(url_for('login'))

            if user_role not in roles:
                return abort(403)  # Forbidden

            return view_func(*args, **kwargs)
        return wrapper
    return decorator
