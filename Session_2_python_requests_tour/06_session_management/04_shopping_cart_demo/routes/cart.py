# routes/cart.py
from flask import Blueprint, request, session, redirect, url_for

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/add_to_cart')
def add_to_cart():
    item = request.args.get('item')
    if not item:
        return "Please specify an item using /add_to_cart?item=ITEMNAME"

    # Initialize cart if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []

    # Add item to cart
    cart = session['cart']
    cart.append(item)
    session['cart'] = cart
    return f"Item '{item}' added to cart.<br><a href='/view_cart'>View Cart</a>"


@cart_bp.route('/view_cart')
def view_cart():
    cart = session.get('cart', [])
    if not cart:
        return "Your cart is empty.<br><a href='/add_to_cart?item=apple'>Add an item</a>"

    items = '<br>'.join(cart)
    return f"Items in cart:<br>{items}<br><a href='/clear_cart'>Clear Cart</a>"


@cart_bp.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return "Cart cleared.<br><a href='/view_cart'>View Cart</a>"
