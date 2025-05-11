import os
import sys
from flask import Flask, jsonify, redirect, url_for
from flask import request
from services.user_service import register_user
from flask import session
from services.user_service import validate_user
from flask import render_template
from services.product_service import get_all_products, get_product_by_id
from services.order_service import save_order, get_orders_by_user

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        if not user_data['username'] or not user_data['email'] or not user_data['password']:
            return render_template('register.html', error="All fields are required")

        success, error = register_user(user_data)
        if success:
            return redirect(url_for('login'))  # or show a success message
        else:
            return render_template('register.html', error=error)

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = validate_user(username, password)
        if user:
            session['username'] = username
            return redirect('/profile')
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


@app.route('/profile')
def profile():
    username = session.get('username')
    if not username:
        return redirect('/login')

    return f"""
    <h2>Welcome, {username}!</h2>
    <p><a href='/products'>Go to Products</a></p>
    <p><a href='/orders'>View Order History</a></p>
    <p><a href='/logout'>Logout</a></p>
    """


@app.route('/inspect', methods=['GET'])
def inspect_request():
    headers = dict(request.headers)
    cookies = request.cookies

    return {
        "received_headers": {
            "X-App-Client": headers.get("X-App-Client"),
            "X-Theme": headers.get("X-Theme")
        },
        "received_cookies": {
            "preferred_currency": cookies.get("preferred_currency"),
            "cart_hint": cookies.get("cart_hint")
        }
    }, 200

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/products', methods=['GET'])
def display_products():
    products = get_all_products()
    return render_template('products.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'username' not in session:
        return redirect('/login')

    product_id = int(request.form.get('product_id'))
    product = get_product_by_id(product_id)

    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
        return redirect('/products')
    else:
        return "Product not found", 404

@app.route('/view_cart')
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = int(request.form.get('product_id'))
    cart = session.get('cart', [])

    # Remove only the first matching item (for quantity handling)
    for i, item in enumerate(cart):
        if item['id'] == product_id:
            del cart[i]
            break

    session['cart'] = cart
    return redirect('/view_cart')


@app.route('/checkout', methods=['POST'])
def checkout():
    username = session.get('username')
    if not username:
        return redirect('/login')

    cart = session.get('cart', [])
    if not cart:
        return "Cart is empty.", 400

    order = save_order(username, cart)
    session.pop('cart', None)  # Clear cart
    return render_template('order_success.html', order=order)

@app.route('/orders')
def view_orders():
    username = session.get('username')
    if not username:
        return redirect('/login')

    orders = get_orders_by_user(username)
    return render_template('orders.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)
