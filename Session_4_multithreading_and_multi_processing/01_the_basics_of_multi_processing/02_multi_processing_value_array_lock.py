import multiprocessing
import time

# Function to increment a shared Value
def increment_counter(shared_counter):
    for _ in range(1000):
        with shared_counter.get_lock():  # Lock ensures safe updates
            shared_counter.value += 1

# Function to multiply elements of shared Array
def multiply_array(shared_array):
    for i in range(len(shared_array)):
        with shared_array.get_lock():  # Lock ensures safe update
            shared_array[i] *= 2

if __name__ == '__main__':
    # Create a shared Value (integer, initialized to 0)
    counter = multiprocessing.Value('i', 0)  # 'i' means integer

    # Create a shared Array of 5 integers [1, 2, 3, 4, 5]
    array = multiprocessing.Array('i', [1, 2, 3, 4, 5])

    # -------- Shared Value Demo --------
    print("\nIncrementing Shared Counter in 4 Processes")
    processes = [multiprocessing.Process(target=increment_counter, args=(counter,)) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Final Counter Value (Expected 4000):", counter.value)

    # -------- Shared Array Demo --------
    print("\nMultiplying Array Elements in 2 Processes")
    processes = [multiprocessing.Process(target=multiply_array, args=(array,)) for _ in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Final Array Values (Expected [4, 8, 12, 16, 20]):", list(array))
