# app.py
from flask import Flask, redirect, url_for
from config import SECRET_KEY, PERMANENT_SESSION_LIFETIME
from routes import auth_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.permanent_session_lifetime = PERMANENT_SESSION_LIFETIME

app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
