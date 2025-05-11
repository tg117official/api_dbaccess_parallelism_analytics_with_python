# services/product_service.py
from file_utils import load_json, write_json

PRODUCT_FILE = 'data/products.json'

def get_all_products():
    return load_json(PRODUCT_FILE)

def get_product_by_id(product_id):
    products = load_json(PRODUCT_FILE)
    return next((p for p in products if p['id'] == product_id), None)

def update_product_stock(product_id, quantity):
    products = load_json(PRODUCT_FILE)
    updated = False
    for product in products:
        if product['id'] == product_id:
            product['stock'] = product.get('stock', 0) - quantity
            updated = True
            break
    if updated:
        write_json(PRODUCT_FILE, products)
    return updated
