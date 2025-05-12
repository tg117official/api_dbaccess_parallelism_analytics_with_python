# scripts/seed_mock_data.py
from datetime import datetime
import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="ecom_db",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

def seed_data():
    with get_connection() as conn:
        with conn.cursor() as cur:

            # --- Users ---
            users = [
                ('admin', 'admin@ex.com', 'adminpass', 'admin'),
                ('seller1', 'seller1@example.com', 'sellerpass', 'seller'),
                ('customer1', 'cust1@example.com', 'custpass', 'customer')
            ]

            for username, email, password, role in users:
                cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
                if not cur.fetchone():
                    cur.execute("""
                        INSERT INTO users (username, email, password, role)
                        VALUES (%s, %s, %s, %s)
                    """, (username, email, password, role))

            # --- Products ---
            products = [
                ('Keyboard', 1200.0, 10, 'https://img1.jpg', 'seller1'),
                ('Mouse', 500.0, 25, 'https://img2.jpg', 'seller1'),
                ('Monitor', 8000.0, 5, 'https://img3.jpg', 'seller1')
            ]

            for name, price, stock, image_url, seller in products:
                cur.execute("""
                    SELECT 1 FROM products
                    WHERE name = %s AND seller = %s
                """, (name, seller))
                if not cur.fetchone():
                    cur.execute("""
                        INSERT INTO products (name, price, stock, image_url, seller)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (name, price, stock, image_url, seller))

            # --- Fetch product IDs for order creation ---
            cur.execute("SELECT id, name, price FROM products WHERE seller = 'seller1' LIMIT 2")
            product_rows = cur.fetchall()
            if not product_rows:
                raise Exception("No products found to attach to an order")

            # --- Orders ---
            cur.execute("SELECT 1 FROM orders WHERE username = 'customer1'")
            if not cur.fetchone():
                cur.execute("""
                    INSERT INTO orders (username, order_time)
                    VALUES (%s, %s)
                    RETURNING id
                """, ('customer1', datetime.now()))
                order_id = cur.fetchone()[0]

                for product in product_rows:
                    product_id, name, price = product
                    cur.execute("""
                        INSERT INTO order_items (order_id, product_id, name, price, quantity)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (order_id, product_id, name, price, 1))

        conn.commit()
        print("Mock data inserted successfully.")

if __name__ == '__main__':
    seed_data()
