import time
import random

# Generate a list of 1,000,000 tuples
out_list = [(random.randint(1, 100), random.randint(1, 1000)) for _ in range(10000000)]

# Time the sorting with negation
start_time = time.time()
out_list.sort(key=lambda x: -x[1])
negation_time = time.time() - start_time

print(f"Negation-based sorting took {negation_time:.4f} seconds.")

# Generate the list again for a fresh start
out_list = [(random.randint(1, 100), random.randint(1, 1000)) for _ in range(10000000)]

# Time the sorting with reverse=True
start_time = time.time()
out_list.sort(key=lambda x: x[1], reverse=True)
reverse_time = time.time() - start_time

print(f"Reverse-based sorting took {reverse_time:.4f} seconds.")
