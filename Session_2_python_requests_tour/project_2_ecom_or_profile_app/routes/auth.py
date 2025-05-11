# routes/auth.py
from flask import Blueprint, render_template, request, session, redirect, url_for
from Session_2_python_requests_tour.project_2_ecom_or_profile_app.services import load_json

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users = load_json('data/users.json')
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)

        if user:
            session['username'] = username
            session['role'] = user.get('role', 'user')
            session.permanent = True
            return redirect(url_for('auth.dashboard'))
        else:
            error = "Invalid credentials"

    return render_template('login.html', error=error)

@auth_bp.route('/dashboard')
def dashboard():
    username = session.get('username')
    role = session.get('role')
    if not username:
        return redirect(url_for('auth.login'))

    return render_template('dashboard.html', username=username, role=role)

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
