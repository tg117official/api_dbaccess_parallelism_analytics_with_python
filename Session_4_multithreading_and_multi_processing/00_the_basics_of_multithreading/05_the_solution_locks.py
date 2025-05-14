import threading
import time

# A Lock ensures that only one thread accesses or modifies the shared resource (shared_data) at a time.
# The with data_lock: block ensures thread-safe access.

# Shared list (simulated data store)
shared_data = []

# Create a lock for synchronizing access to shared_data
data_lock = threading.Lock()

# Function to simulate downloading data
def download_data():
    print("Downloader: Starting download...")
    time.sleep(2)  # Simulate network delay

    # Lock before modifying shared_data
    with data_lock:
        shared_data.append("data_file_1")
        print("Downloader: Data downloaded and added to shared list.")

# Function to simulate processing data
def process_data():
    print("Processor: Waiting for data to process...")
    time.sleep(3)  # Wait for download to complete

    with data_lock:
        if shared_data:
            data = shared_data[0] + "_processed"
            shared_data.append(data)
            print(f"Processor: Processed data added: {data}")
        else:
            print("Processor: No data found to process.")

# Function to simulate uploading data
def upload_data():
    print("Uploader: Waiting for processed data to upload...")
    time.sleep(4)  # Wait for processing to complete

    with data_lock:
        processed = [item for item in shared_data if "processed" in item]
        if processed:
            print(f"Uploader: Uploading {processed[0]} to cloud...")
            time.sleep(1)
            print("Uploader: Upload successful.")
        else:
            print("Uploader: No processed data available to upload.")

# Start measuring time
start_time = time.time()

# Creating threads with different target functions
t1 = threading.Thread(target=download_data)
t2 = threading.Thread(target=process_data)
t3 = threading.Thread(target=upload_data)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

# End measuring time
end_time = time.time()

print(f"\nTotal execution time with synchronization: {end_time - start_time:.2f} seconds")
