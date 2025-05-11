# routes/auth.py
from flask import Blueprint, request, session

auth_bp = Blueprint('auth', __name__)

# Dummy users
users = ["sandeep", "admin", "guest"]

@auth_bp.route('/login')
def login():
    username = request.args.get('username')
    if username in users:
        session['username'] = username
        return f"Hello {username}, you are now logged in. <br><a href='/dashboard'>Go to Dashboard</a>"
    else:
        return "Invalid username. Try: /login?username=sandeep"

@auth_bp.route('/dashboard')
def dashboard():
    username = session.get('username')
    if username:
        return f"Welcome back, {username}! <br><a href='/logout'>Logout</a>"
    else:
        return "You're not logged in. <a href='/login?username=sandeep'>Login</a>"

@auth_bp.route('/logout')
def logout():
    session.clear()
    return "You have been logged out. <br><a href='/login?username=sandeep'>Login again</a>"

@auth_bp.route('/')
def home():
    return '''
    <h2>Flask Session Demo</h2>
    <p>To login, visit: <a href="/login?username=sandeep">/login?username=sandeep</a></p>
    <p>Then visit: <a href="/dashboard">/dashboard</a></p>
    '''
