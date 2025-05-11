# Used when:
    # Working with millions of rows
    # Needing to process batches incrementally (e.g., ETL jobs)
    # Avoiding memory blowups in apps or pipelines


import psycopg2
from psycopg2 import OperationalError

def named_cursor_demo():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname="training_db",
            user="postgres",
            password="your_password",  # Replace securely
            host="localhost",
            port="5432"
        )
        print("Connected to database.")

        # Create large sample table
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS big_demo (
            id SERIAL PRIMARY KEY,
            value TEXT
        );
        """)
        connection.commit()

        # Insert sample data if empty
        cursor.execute("SELECT COUNT(*) FROM big_demo;")
        count = cursor.fetchone()[0]
        if count < 100:
            print("📥 Inserting sample data (100 rows)...")
            sample_data = [(f"Value {i}",) for i in range(1, 101)]
            cursor.executemany("INSERT INTO big_demo (value) VALUES (%s);", sample_data)
            connection.commit()
            print("✅ Data inserted.\n")

        cursor.close()

        # Create a named cursor (server-side)
        print("🚀 Creating named (server-side) cursor...")
        named_cursor = connection.cursor(name='big_cursor')  # key difference
        named_cursor.itersize = 10  # control batch size

        named_cursor.execute("SELECT * FROM big_demo ORDER BY id;")

        print("\nFetching 10 rows at a time:\n")
        batch = named_cursor.fetchmany(10)
        while batch:
            for row in batch:
                print(row)
            input("Press Enter to load next 10 rows...")
            batch = named_cursor.fetchmany(10)

        # Scroll example
        print("\nScrolling back to row 0 and reading 1st 5 again:\n")
        named_cursor.scroll(0, mode='absolute')  # scroll to the start
        for row in named_cursor.fetchmany(5):
            print("Scrolled row:", row)

        # Cleanup
        named_cursor.close()
        connection.close()
        print("\nNamed cursor and connection closed.")

    except OperationalError as e:
        print("Connection or query failed.")
        print(f"Error: {e}")

if __name__ == "__main__":
    named_cursor_demo()
