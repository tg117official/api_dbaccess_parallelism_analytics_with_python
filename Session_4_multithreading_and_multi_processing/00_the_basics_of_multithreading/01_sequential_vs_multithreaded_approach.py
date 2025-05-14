import threading  # Importing threading module for multithreading
import time       # Importing time module to measure execution time

# This is a simple function that simulates a time-consuming task
def task(name):
    print(f"Task {name} started")
    time.sleep(2)  # Simulates work by pausing the program for 2 seconds
    print(f"Task {name} completed")

# ------------------ Sequential Execution ------------------
start_time = time.time()  # Record the start time for sequential execution

# Run tasks one after another (sequentially)
task("A")
task("B")

end_time = time.time()  # Record the end time for sequential execution
print(f"\nSequential execution time: {end_time - start_time:.2f} seconds\n")

# ------------------ Multithreaded Execution ------------------
start_time = time.time()  # Record the start time for multithreaded execution

# Create two threads to run the same function concurrently
thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before moving on
thread1.join()
thread2.join()

end_time = time.time()  # Record the end time for multithreaded execution
print(f"\nMultithreaded execution time: {end_time - start_time:.2f} seconds\n")
