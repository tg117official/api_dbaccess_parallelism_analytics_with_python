# client/download_images.py

import requests
import os

API_URL = "http://localhost:5000/products"
IMAGE_DIR = "static/images"

def download_images():
    # Create directory if it doesn't exist
    os.makedirs(IMAGE_DIR, exist_ok=True)

    # Step 1: Get the product list from the API
    response = requests.get(API_URL)
    if response.status_code != 200:
        print("Failed to fetch products.")
        return

    products = response.json()

    # Step 2: Loop through products and download images
    for product in products:
        image_url = product.get("image_url")
        product_id = product.get("id")
        if image_url:
            try:
                image_data = requests.get(image_url).content
                file_path = os.path.join(IMAGE_DIR, f"{product_id}_{product['name'].replace(' ', '_')}.jpg")
                with open(file_path, "wb") as img_file:
                    img_file.write(image_data)
                print(f"Downloaded: {file_path}")
            except Exception as e:
                print(f"Failed to download image for product {product['id']}: {e}")

if __name__ == '__main__':
    download_images()
