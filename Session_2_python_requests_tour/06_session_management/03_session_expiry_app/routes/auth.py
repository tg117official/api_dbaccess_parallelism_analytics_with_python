# routes/auth.py
from flask import Blueprint, render_template, request, session, redirect, url_for

auth_bp = Blueprint('auth', __name__)

# Dummy user database
users = {
    "sandeep": "password123",
    "admin": "adminpass"
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if users.get(username) == password:
            session.permanent = True  # Make the session use configured lifetime
            session['username'] = username
            return redirect(url_for('auth.dashboard'))
        else:
            error = "Invalid username or password."

    return render_template('login.html', error=error)

@auth_bp.route('/dashboard')
def dashboard():
    username = session.get('username')
    if username:
        return f"Welcome {username}!<br><a href='/logout'>Logout</a>"
    return redirect(url_for('auth.login'))

@auth_bp.route('/logout')
def logout():
    session.clear()
    return "You have been logged out.<br><a href='/login'>Login again</a>"
