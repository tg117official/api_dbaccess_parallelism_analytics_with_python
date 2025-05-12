# services/product_service.py

from services.db import get_connection

def get_all_products():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, price, stock, image_url, seller
                FROM products
                ORDER BY id
            """)
            rows = cur.fetchall()
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "price": row[2],
                    "stock": row[3],
                    "image_url": row[4],
                    "seller": row[5]
                }
                for row in rows
            ]


def get_product_by_id(product_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, price, stock, image_url, seller
                FROM products
                WHERE id = %s
            """, (product_id,))
            row = cur.fetchone()
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "price": row[2],
                    "stock": row[3],
                    "image_url": row[4],
                    "seller": row[5]
                }
    return None


def get_products_by_seller(seller_username):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, price, stock, image_url, seller
                FROM products
                WHERE seller = %s
                ORDER BY id
            """, (seller_username,))
            rows = cur.fetchall()
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "price": row[2],
                    "stock": row[3],
                    "image_url": row[4],
                    "seller": row[5]
                }
                for row in rows
            ]


def add_product(product):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO products (name, price, stock, image_url, seller)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                product['name'],
                product['price'],
                product['stock'],
                product['image_url'],
                product['seller']
            ))
            conn.commit()


def update_product(product_id, updated_data):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE products
                SET name = %s, price = %s, stock = %s, image_url = %s
                WHERE id = %s
            """, (
                updated_data['name'],
                updated_data['price'],
                updated_data['stock'],
                updated_data['image_url'],
                product_id
            ))
            conn.commit()


def delete_product(product_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
            conn.commit()


def delete_products_by_seller(seller_username):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE seller = %s", (seller_username,))
            conn.commit()
