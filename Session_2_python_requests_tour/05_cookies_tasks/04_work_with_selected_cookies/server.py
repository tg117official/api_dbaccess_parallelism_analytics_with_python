from flask import Flask, request, make_response

app = Flask(__name__)

# Set multiple cookies
@app.route('/set_cookies')
def set_cookies():
    resp = make_response("Multiple cookies set.")
    resp.set_cookie("user", "sandeep")
    resp.set_cookie("theme", "dark")
    resp.set_cookie("token", "abc123")
    return resp

# Read only selected cookie
@app.route('/read_selected_cookie')
def read_selected_cookie():
    user_cookie = request.cookies.get("user", "Not Found")
    return f"'user' cookie: {user_cookie}"

if __name__ == '__main__':
    app.run(debug=True)
