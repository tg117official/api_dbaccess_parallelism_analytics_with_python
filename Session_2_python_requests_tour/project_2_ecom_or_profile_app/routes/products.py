# routes/products.py
from flask import Blueprint, jsonify
from Session_2_python_requests_tour.project_2_ecom_or_profile_app.services import load_json

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def list_products():
    products = load_json('data/products.json')
    return jsonify(products)
