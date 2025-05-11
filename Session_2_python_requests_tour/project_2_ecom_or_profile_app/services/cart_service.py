# services/cart_service.py
from flask import session

def get_cart():
    return session.get('cart', [])

def add_to_cart(item):
    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart
    return cart

def clear_cart():
    session.pop('cart', None)
    return []
