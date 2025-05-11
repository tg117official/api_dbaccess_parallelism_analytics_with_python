from flask import Flask, request, make_response
from datetime import datetime, timedelta

app = Flask(__name__)

# Dummy user database
valid_users = {
    "sandeep": "password123",
    "admin": "adminpass"
}

# POST Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    remember = request.form.get("remember_me")

    if valid_users.get(username) == password:
        resp = make_response(f"Welcome, {username}!")

        # Persistent cookie if 'remember me' is checked
        if remember == "true":
            expires = datetime.now() + timedelta(days=7)
            resp.set_cookie("logged_in_user", username, expires=expires)
        else:
            resp.set_cookie("logged_in_user", username)  # Session cookie

        return resp
    else:
        return "Invalid credentials", 401

# Protected route
@app.route('/protected')
def protected():
    user = request.cookies.get("logged_in_user")
    if user:
        return f"Hello {user}, you are remembered."
    else:
        return "Please log in.", 401

# Logout
@app.route('/logout')
def logout():
    resp = make_response("Logged out successfully.")
    resp.delete_cookie("logged_in_user")
    return resp

if __name__ == '__main__':
    app.run(debug=True)
