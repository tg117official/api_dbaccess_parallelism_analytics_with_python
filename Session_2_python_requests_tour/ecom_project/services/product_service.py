# services/product_service.py
from services.file_utils import load_json

PRODUCTS_FILE = 'data/products.json'

def get_all_products():
    return load_json(PRODUCTS_FILE)

def get_product_by_id(product_id):
    products = load_json(PRODUCTS_FILE)
    return next((p for p in products if p['id'] == product_id), None)

