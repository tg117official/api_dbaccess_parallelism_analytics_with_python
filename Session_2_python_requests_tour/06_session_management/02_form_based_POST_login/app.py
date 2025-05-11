# app.py
from flask import Flask, redirect, url_for
from config import SECRET_KEY
from routes import auth_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Register Blueprints
app.register_blueprint(auth_bp)
# Flask includes all the routes and logic defined in the auth_bp BlueprintFlask
# includes all the routes and logic defined in the auth_bp Blueprint
# These routes work as if they were defined in app.py, but they’re modularized

@app.route('/')
def home():
    return redirect(url_for('auth.login'))
# 'auth' is the name of the Blueprint
# 'login' is the name of the view function inside that Blueprint

if __name__ == '__main__':
    app.run(debug=True)
