import threading  # Importing threading module to run tasks in parallel
import time       # Importing time module to measure execution time

# Function that simulates a time-consuming task
def task(name):
    print(f"Task {name} started")
    time.sleep(2)  # Simulates a 2-second task (e.g., downloading, processing)
    print(f"Task {name} completed")

# ------------------ Sequential Execution ------------------
start_time = time.time()  # Start time for sequential execution

# Run 10 tasks one after another (total ~20 seconds)
for i in range(10):
    task(f"{i+1}")  # Call task function with a unique task number

end_time = time.time()  # End time for sequential execution
print(f"\nSequential execution time: {end_time - start_time:.2f} seconds\n")

# ------------------ Multithreaded Execution ------------------
start_time = time.time()  # Start time for multithreaded execution

threads = []  # List to keep track of all thread objects

# Create and start 10 threads (tasks run concurrently)
for i in range(10):
    thread = threading.Thread(target=task, args=(f"{i+1}",))  # Create thread
    thread.start()  # Start the thread
    threads.append(thread)  # Add thread to the list

# Wait for all threads to complete
for thread in threads:
    thread.join()  # Block until the thread finishes

end_time = time.time()  # End time for multithreaded execution
print(f"\nMultithreaded execution time: {end_time - start_time:.2f} seconds\n")
