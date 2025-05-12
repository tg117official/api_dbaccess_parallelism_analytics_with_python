import psycopg2
from psycopg2 import sql

def get_connection():
    return psycopg2.connect(
        dbname="ecom_db",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
