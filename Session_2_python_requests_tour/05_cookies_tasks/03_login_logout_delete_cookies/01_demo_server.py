from flask import Flask, request, make_response

app = Flask(__name__)

valid_users = {
    "sandeep": "password123",
    "admin": "adminpass"
}

# 🔐 Login Route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if valid_users.get(username) == password:
        resp = make_response(f"✅ Welcome, {username}!")
        resp.set_cookie("logged_in_user", username)
        return resp
    else:
        return "❌ Invalid credentials", 401

# 🔒 Protected Route
@app.route('/protected')
def protected():
    user = request.cookies.get("logged_in_user")
    if user:
        return f"🔐 Hello {user}, you are logged in."
    else:
        return "🔒 Access denied. Please log in.", 401

# 🔓 Logout Route
@app.route('/logout')
def logout():
    resp = make_response("✅ You have been logged out.")
    resp.delete_cookie("logged_in_user")
    return resp

if __name__ == '__main__':
    app.run(debug=True)
