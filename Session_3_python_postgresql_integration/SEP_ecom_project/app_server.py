# -----------------------
# Standard Library Imports
# -----------------------
import os
import sys
from datetime import datetime, timedelta

# -----------------------
# Flask Core
# -----------------------
from flask import Flask, request, session, render_template, redirect, url_for, jsonify

# -----------------------
# Internal Service Imports
# -----------------------
from services.access_control import role_required
from services.update_service import update_user
from services.user_service import (
    register_user, get_user_by_username, delete_user,
    validate_user, get_all_users, update_user_role
)
from services.product_service import (
    get_all_products, get_product_by_id, get_products_by_seller,
    delete_products_by_seller, add_product, update_product, delete_product
)
from services.order_service import save_order, get_orders_by_user

# -----------------------
# App Configuration
# -----------------------
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.permanent_session_lifetime = timedelta(days=7)

# -----------------------
# DB Connection and Init
# _______________________

from services.schema import initialize_schema
initialize_schema()

# -----------------------
# Home Page
# -----------------------
@app.route('/')
def home():
    username = session.get('username')
    role = session.get('role')

    if username and role:
        if role == 'admin':
            return redirect('/admin')
        elif role == 'seller':
            return redirect('/seller')
        else:
            return redirect('/customer')

    return render_template('home.html')

# -----------------------
# Authentication Routes
# -----------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "role": "customer"
        }

        if not user_data['username'] or not user_data['email'] or not user_data['password']:
            return render_template('register.html', error="All fields are required")

        success, error = register_user(user_data)
        if success:
            return redirect(url_for('login'))
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
            session.permanent = True
            session['username'] = username
            session['login_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            session['role'] = user['role']

            if user['role'] == 'admin':
                return redirect('/admin')
            elif user['role'] == 'seller':
                return redirect('/seller')
            else:
                return redirect('/customer')

        return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# -----------------------
# Customer Routes
# -----------------------
@app.route('/customer')
@role_required('customer')
def customer_dashboard():
    username = session.get('username')
    uname = username.capitalize()
    return render_template('customer_dashboard.html', username=uname)

# -----------------------
# Seller Routes
# -----------------------
@app.route('/seller')
@role_required('seller')
def seller_dashboard():
    username = session.get('username').capitalize()
    return render_template('seller_dashboard.html', uname=username)

@app.route('/seller/products')
@role_required('seller')
def seller_product_catalog():
    seller = session.get('username')
    products = get_products_by_seller(seller)
    return render_template('seller/catalog.html', products=products)

@app.route('/manage/products')
@role_required('seller')
def manage_products():
    seller = session.get('username')
    products = get_products_by_seller(seller)
    return render_template('seller/manage_products.html', products=products)

@app.route('/manage/products/add', methods=['GET', 'POST'])
@role_required('seller')
def add_product_view():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))
        stock = int(request.form.get('stock'))
        image_url = request.form.get('image_url')
        seller = session.get('username')

        new_product = {
            "name": name,
            "price": price,
            "stock": stock,
            "image_url": image_url,
            "seller": seller
        }

        add_product(new_product)
        return redirect('/manage/products')

    return render_template('seller/add_product.html')


@app.route('/manage/products/edit/<int:product_id>', methods=['GET', 'POST'])
@role_required('seller')
def edit_product_view(product_id):
    product = get_product_by_id(product_id)
    if not product or product.get('seller') != session.get('username'):
        return "Unauthorized or Product not found", 403

    if request.method == 'POST':
        product['name'] = request.form.get('name')
        product['price'] = float(request.form.get('price'))
        product['stock'] = int(request.form.get('stock'))
        product['image_url'] = request.form.get('image_url')

        update_product(product_id, product)
        return redirect('/manage/products')

    return render_template('seller/edit_product.html', product=product)

@app.route('/manage/products/delete/<int:product_id>', methods=['POST'])
@role_required('seller')
def delete_product_view(product_id):
    delete_product(product_id)
    return redirect('/manage/products')

# -----------------------
# Admin Routes
# -----------------------
@app.route('/admin')
@role_required('admin')
def admin_panel():
    username = session.get('username').capitalize()
    return render_template('admin_dashboard.html', username=username)

@app.route('/admin/users')
@role_required('admin')
def admin_users():
    users = get_all_users()
    return render_template('admin/users.html', users=users)

@app.route('/admin/users/edit/<username>', methods=['GET', 'POST'])
@role_required('admin')
def edit_user_role(username):
    user = get_user_by_username(username)
    if not user:
        return "User not found", 404

    if request.method == 'POST':
        new_role = request.form.get('role')
        update_user_role(username, new_role)
        return redirect('/admin/users')

    return render_template('admin/edit_user.html', user=user)

@app.route('/admin/users/delete/<username>', methods=['POST'])
@role_required('admin')
def delete_user_by_admin(username):
    current_user = session.get('username')

    if username == current_user:
        return "<h3>❌ You cannot delete your own admin account. <a href='/admin/users'>Back</a></h3>"

    user = get_user_by_username(username)
    if user:
        if user['role'] == 'seller':
            delete_products_by_seller(username)
        delete_user(username)

    return redirect('/admin/users')

# -----------------------
# Profile & Session Management
# -----------------------
@app.route('/profile')
def profile():
    username = session.get('username')
    login_time = session.get('login_time')
    role = session.get('role')
    return render_template('profile/profile.html', username=username, login_time=login_time, role=role)

@app.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
    username = session.get('username')
    if not username:
        return redirect('/login')

    user = get_user_by_username(username)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        update_user(username, {
            'email': email,
            'password': password
        })

        return redirect('/profile')

    return render_template('profile/edit_profile.html', user=user)

@app.route('/profile/delete', methods=['GET', 'POST'])
def delete_profile():
    username = session.get('username')
    role = session.get('role')

    if not username:
        return redirect('/login')

    if role == 'admin':
        return "<h3>❌ Admin accounts cannot be deleted. <a href='/profile'>Go back</a></h3>"

    if request.method == 'POST':
        delete_user(username)

        if role == 'seller':
            delete_products_by_seller(username)

        session.clear()
        return "<h3>Your account has been deleted. <a href='/'>Go Home</a></h3>"

    return render_template('profile/confirm_delete.html', username=username, role=role)

# -----------------------
# Product Browsing & Cart
# -----------------------
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

    for i, item in enumerate(cart):
        if item['id'] == product_id:
            del cart[i]
            break

    session['cart'] = cart
    return redirect('/view_cart')

# -----------------------
# Orders
# -----------------------
@app.route('/checkout', methods=['POST'])
def checkout():
    username = session.get('username')
    if not username:
        return redirect('/login')

    cart = session.get('cart', [])
    if not cart:
        return "Cart is empty.", 400

    order = save_order(username, cart)
    session.pop('cart', None)
    return render_template('order_success.html', order=order)

@app.route('/orders')
def view_orders():
    username = session.get('username')
    if not username:
        return redirect('/login')

    orders = get_orders_by_user(username)
    return render_template('orders.html', orders=orders)

# -----------------------
# Debug / Utility Route
# -----------------------
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

# -----------------------
# Error Handlers
# -----------------------
@app.errorhandler(403)
def forbidden(e):
    return "<h2>403 Forbidden</h2><p>You do not have permission to access this page.</p>", 403

# -----------------------
# Run the App
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)
