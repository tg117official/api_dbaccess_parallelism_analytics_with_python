from flask import Flask, make_response, request
from datetime import datetime, timedelta

# Secure    – sends the cookie only over HTTPS
# HttpOnly  – blocks JavaScript access
# Expires / Max-Age – sets duration
# Path      – restricts cookie to a specific route

app = Flask(__name__)

# Route to set various cookies with flags
@app.route('/set_cookies')
def set_cookies():
    response = make_response("Cookies set with flags!")

    # 1. Cookie with max-age (expires in 2 minutes)
    response.set_cookie(
        "short_lived", "value1", max_age=120  # 120 seconds
    )

    # 2. Cookie with expires (exact date)
    expires = datetime.now() + timedelta(minutes=5)
    response.set_cookie(
        "expires_cookie", "value2", expires=expires
    )

    # 3. Cookie with HttpOnly flag
    response.set_cookie(
        "http_only_cookie", "secret", httponly=True
    )

    # 4. Cookie with Secure flag (Note: requires HTTPS)
    response.set_cookie(
        "secure_cookie", "secure_value", secure=True
    )

    # 5. Cookie limited to /only_here path
    response.set_cookie(
        "path_cookie", "scoped_value", path="/only_here"
    )

    return response

# Route that returns all cookies
@app.route('/show_cookies')
def show_cookies():
    return {
        "received_cookies": dict(request.cookies)
    }

# Route that has access to "path_cookie"
@app.route('/only_here')
def only_here():
    return {
        "cookies_here": dict(request.cookies)
    }

# Route to demonstrate JavaScript can't access HttpOnly cookies
@app.route('/client_script')
def client_script():
    return """
    <html><body>
    <script>
    document.write("Cookies visible to JS: " + document.cookie);
    </script>
    </body></html>
    """

if __name__ == '__main__':
    app.run(debug=True)
