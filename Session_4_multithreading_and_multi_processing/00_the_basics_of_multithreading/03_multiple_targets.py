import threading
import time

# Simulated task 1
def download_file():
    print("Downloading file...")
    time.sleep(2)
    print("File downloaded.")

# Simulated task 2
def process_data():
    print("Processing data...")
    time.sleep(3)
    print("Data processed.")

# Simulated task 3
def upload_to_cloud():
    print("Uploading to cloud...")
    time.sleep(1)
    print("Upload complete.")

# Start time
start_time = time.time()

# Creating threads with different target functions
t1 = threading.Thread(target=download_file)
t2 = threading.Thread(target=process_data)
t3 = threading.Thread(target=upload_to_cloud)

# Start all threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

# End time
end_time = time.time()

print(f"\nTotal time with multithreading: {end_time - start_time:.2f} seconds")
