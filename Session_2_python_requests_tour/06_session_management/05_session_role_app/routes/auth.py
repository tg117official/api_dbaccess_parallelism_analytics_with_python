
# routes/auth.py
from flask import Blueprint, render_template, request, session, redirect, url_for

auth_bp = Blueprint('auth', __name__)

# Dummy users and their roles
users = {
    "sandeep": {"password": "password123", "role": "admin"},
    "john": {"password": "johnpass", "role": "user"}
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = users.get(username)
        if user and user["password"] == password:
            session['username'] = username
            session['role'] = user["role"]
            return redirect(url_for('auth.dashboard'))
        else:
            error = "Invalid username or password"

    return render_template('login.html', error=error)

@auth_bp.route('/dashboard')
def dashboard():
    username = session.get("username")
    role = session.get("role")

    if not username:
        return redirect(url_for('auth.login'))

    if role == "admin":
        return f"Admin Dashboard: Welcome {username}.<br><a href='/logout'>Logout</a>"
    elif role == "user":
        return f"User Dashboard: Hello {username}.<br><a href='/logout'>Logout</a>"
    else:
        return "Unknown role."

@auth_bp.route('/logout')
def logout():
    session.clear()
    return "You have been logged out.<br><a href='/login'>Login again</a>"
