# app.py
from flask import Flask
from config import SECRET_KEY
from routes import cart_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(cart_bp)

@app.route('/')
def home():
    return '''
    <h2>Shopping Cart Demo</h2>
    <p>Try: <a href="/add_to_cart?item=apple">/add_to_cart?item=apple</a></p>
    <p>Then visit: <a href="/view_cart">/view_cart</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
