# routes/cart.py
from flask import Blueprint, session, request, jsonify

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_to_cart')
def add_to_cart():
    item = request.args.get('item')
    if not item:
        return "Please provide ?item=item_name", 400

    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart
    return jsonify({"cart": cart})

@cart_bp.route('/view_cart')
def view_cart():
    return jsonify({"cart": session.get('cart', [])})

@cart_bp.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return jsonify({"message": "Cart cleared"})
