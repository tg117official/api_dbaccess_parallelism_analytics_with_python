from flask import Flask
from config import SECRET_KEY, PERMANENT_SESSION_LIFETIME
from routes import *

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.permanent_session_lifetime = PERMANENT_SESSION_LIFETIME

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)


@app.before_request
def refresh_session():
    # Keep session alive while user is active
    from flask import session
    session.permanent = True

if __name__ == '__main__':
    app.run(debug=True)
