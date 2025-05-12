# services/order_service.py

from services.db import get_connection
from datetime import datetime

def save_order(username, cart):
    """
    Saves a new order and associated order items.
    Returns the order info and items.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Insert into orders table
            cur.execute("""
                INSERT INTO orders (username, order_time)
                VALUES (%s, %s)
                RETURNING id, order_time
            """, (username, datetime.now()))
            order_row = cur.fetchone()
            order_id = order_row[0]
            order_time = order_row[1]

            # Insert order items
            for item in cart:
                cur.execute("""
                    INSERT INTO order_items (order_id, product_id, name, price, quantity)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    order_id,
                    item['id'],
                    item['name'],
                    item['price'],
                    1  # assuming quantity = 1 per add_to_cart action
                ))

        conn.commit()
        return {
            "id": order_id,
            "user": username,
            "items": cart,
            "timestamp": order_time.isoformat()
        }


def get_orders_by_user(username):
    """
    Fetches orders and their items for a given user.
    Returns a list of orders with item details.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Get all orders for the user
            cur.execute("""
                SELECT id, order_time FROM orders
                WHERE username = %s
                ORDER BY order_time DESC
            """, (username,))
            order_rows = cur.fetchall()

            orders = []
            for order in order_rows:
                order_id = order[0]
                order_time = order[1]

                # Get items for each order
                cur.execute("""
                    SELECT product_id, name, price, quantity
                    FROM order_items
                    WHERE order_id = %s
                """, (order_id,))
                item_rows = cur.fetchall()
                items = [
                    {
                        "id": item[0],
                        "name": item[1],
                        "price": item[2],
                        "quantity": item[3]
                    }
                    for item in item_rows
                ]

                orders.append({
                    "id": order_id,
                    "user": username,
                    "timestamp": order_time.isoformat(),
                    "items": items
                })

            return orders
