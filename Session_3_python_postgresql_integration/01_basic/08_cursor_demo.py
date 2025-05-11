import psycopg2
from psycopg2 import OperationalError

def demonstrate_cursors():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            dbname="training_db",
            user="postgres",
            password="your_password",  # Replace securely
            host="localhost",
            port="5432"
        )

        print("Connected to training_db\n")
        cursor = connection.cursor()

        # CREATE TABLE IF NOT EXISTS
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS demo_cursor (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL
        );
        """)
        connection.commit()
        print("Table 'demo_cursor' created (if not exists).")

        # INSERT SAMPLE DATA
        print("Inserting sample records...")
        cursor.execute("DELETE FROM demo_cursor;")  # clear for demo
        sample_data = [("Task A",), ("Task B",), ("Task C",)]
        cursor.executemany("INSERT INTO demo_cursor (title) VALUES (%s);", sample_data)
        connection.commit()
        print("Sample data inserted.\n")

        # FETCH ALL ROWS
        print("Fetching all rows:")
        cursor.execute("SELECT * FROM demo_cursor;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        #FETCH ONE
        print("\nFetching just one row:")
        cursor.execute("SELECT * FROM demo_cursor;")
        one_row = cursor.fetchone()
        print("First row:", one_row)

        #FETCH MANY (e.g., 2 rows)
        print("\nFetching two rows:")
        cursor.execute("SELECT * FROM demo_cursor;")
        two_rows = cursor.fetchmany(2)
        print("Two rows:", two_rows)

        # USING CURSOR AS AN ITERATOR
        print("\nIterating using cursor:")
        cursor.execute("SELECT * FROM demo_cursor;")
        for row in cursor:
            print("Iterated row:", row)

        # RESETTING A CURSOR
        # The execute() method overwrites the previous query results (if any).
        # The cursor is reused to run a completely new SQL statement.
        print("\nReusing cursor for another query:")
        cursor.execute("SELECT COUNT(*) FROM demo_cursor;")
        count = cursor.fetchone()
        print("Total records:", count[0])

        # CLEANUP
        cursor.close()
        print("\nCursor closed manually.")

        # USING WITH STATEMENT (auto-close)
        print("\nUsing 'with' for context-managed cursor:")
        with connection.cursor() as cur:
            cur.execute("SELECT title FROM demo_cursor;")
            titles = cur.fetchall()
            for t in titles:
                print("Title from with-cursor:", t[0])

        connection.close()
        print("\nConnection closed.")

    except OperationalError as e:
        print("Database connection or query failed.")
        print(f"Error: {e}")

if __name__ == "__main__":
    demonstrate_cursors()
