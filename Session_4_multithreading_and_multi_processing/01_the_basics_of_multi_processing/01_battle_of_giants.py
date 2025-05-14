import time
import threading
import multiprocessing

# Function to count primes
def count_primes(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    print(f"Primes below {n}: {count}")

# Check if number is prime
def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Main block to safely run multiprocessing code
if __name__ == '__main__':
    numbers = [500000, 150000, 550000, 655000]

    # -------- Sequential --------
    start = time.time()
    for n in numbers:
        count_primes(n)
    print(f"\nSequential execution took: {time.time() - start:.2f} seconds\n")

    # -------- Multithreading --------
    start = time.time()
    threads = []
    for n in numbers:
        t = threading.Thread(target=count_primes, args=(n,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print(f"Multithreading execution took: {time.time() - start:.2f} seconds\n")

    # -------- Multiprocessing --------
    start = time.time()
    processes = []
    for n in numbers:
        p = multiprocessing.Process(target=count_primes, args=(n,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    print(f"Multiprocessing execution took: {time.time() - start:.2f} seconds\n")
