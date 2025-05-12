from services.file_utils import load_json, write_json

PRODUCTS_FILE = 'data/products.json'

def get_all_products():
    return load_json(PRODUCTS_FILE)

def get_product_by_id(product_id):
    products = load_json(PRODUCTS_FILE)
    return next((p for p in products if p['id'] == product_id), None)

def get_products_by_seller(seller_username):
    products = load_json(PRODUCTS_FILE)
    return [p for p in products if p.get('seller') == seller_username]


def add_product(product):
    products = load_json(PRODUCTS_FILE)
    product['id'] = max([p['id'] for p in products], default=0) + 1
    products.append(product)
    write_json(PRODUCTS_FILE, products)

def update_product(product_id, updated_data):
    products = load_json(PRODUCTS_FILE)
    for p in products:
        if p['id'] == product_id:
            p.update(updated_data)
            break
    write_json(PRODUCTS_FILE, products)

def delete_product(product_id):
    products = load_json(PRODUCTS_FILE)
    products = [p for p in products if p['id'] != product_id]
    write_json(PRODUCTS_FILE, products)


def delete_products_by_seller(seller_username):
    products = load_json(PRODUCTS_FILE)
    products = [p for p in products if p.get('seller') != seller_username]
    write_json(PRODUCTS_FILE, products)
