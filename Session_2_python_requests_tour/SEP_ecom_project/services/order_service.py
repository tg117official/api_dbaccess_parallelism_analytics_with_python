# services/order_service.py
from services.file_utils import load_json, write_json
from datetime import datetime

ORDER_FILE = 'data/orders.json'


def save_order(username, cart):
    orders = load_json(ORDER_FILE)

    new_order = {
        "id": len(orders) + 1,
        "user": username,
        "items": cart,
        "timestamp": datetime.now().isoformat()
    }

    orders.append(new_order)
    write_json(ORDER_FILE, orders)
    return new_order


def get_orders_by_user(username):
    orders = load_json(ORDER_FILE)
    return [o for o in orders if o['user'] == username]
