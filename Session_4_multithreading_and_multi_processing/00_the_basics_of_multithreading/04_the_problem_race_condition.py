import threading
import time

# Shared list (no lock protection here)
shared_data = []

# Function to simulate downloading data
def download_data():
    print("Downloader: Starting download...")
    time.sleep(2)
    shared_data.append("data_file_1")
    print("Downloader: Data downloaded and added to shared list.")

# Function to simulate processing data (no lock!)
def process_data():
    print("Processor: Waiting for data to process...")
    time.sleep(3)
    # Access shared_data without checking if data exists
    try:
        data = shared_data[0] + "_processed"
        shared_data.append(data)
        print(f"Processor: Processed data added: {data}")
    except IndexError:
        print("Processor: ❌ No data found to process due to race condition!")

# Function to simulate uploading data (no lock!)
def upload_data():
    print("Uploader: Waiting for processed data to upload...")
    time.sleep(4)
    processed = [item for item in shared_data if "processed" in item]
    if processed:
        print(f"Uploader: Uploading {processed[0]} to cloud...")
        time.sleep(1)
        print("Uploader: Upload successful.")
    else:
        print("Uploader: ❌ No processed data available to upload due to race condition!")

# Start measuring time
start_time = time.time()

# Create threads without synchronization
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

print(f"\nTotal execution time WITHOUT synchronization: {end_time - start_time:.2f} seconds")
