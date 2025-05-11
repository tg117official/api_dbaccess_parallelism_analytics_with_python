from flask import Flask, request, make_response

app = Flask(__name__)

# Dummy credentials for login check
valid_users = {
    "sandeep": "password123",
    "admin": "adminpass"
}

# Endpoint: Login (POST)
@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")

    # Simple user validation
    if valid_users.get(username) == password:
        resp = make_response(f"Login successful for {username}")
        resp.set_cookie("logged_in_user", username)
        return resp
    else:
        return "Invalid username or password", 401

# Endpoint: Protected (GET)
@app.route('/protected')
def protected():
    user = request.cookies.get("logged_in_user")
    if user:
        return f"Hello {user}, welcome to the protected resource."
    else:
        return "Access denied. Please login.", 401

if __name__ == '__main__':
    app.run(debug=True)
