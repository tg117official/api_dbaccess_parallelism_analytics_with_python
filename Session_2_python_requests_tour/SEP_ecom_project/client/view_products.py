# client/view_products.py

import requests

# URL of your Flask server
API_URL = "http://localhost:5000/products"

def view_products():
    try:
        response = requests.get(API_URL)

        # Check if the request was successful
        if response.status_code == 200:
            products = response.json()
            print("=== Product Catalog ===")
            for product in products:
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ₹{product['price']}")
                print(f"Stock: {product['stock']}")
                print(f"Image: {product['image_url']}")
                print("-" * 30)
        else:
            print(f"Failed to fetch products. Status code: {response.status_code}")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    view_products()
