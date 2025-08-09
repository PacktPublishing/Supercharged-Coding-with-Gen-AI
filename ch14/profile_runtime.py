import time
from fibonacci import fibonacci_recursive, fibonacci_iterative

n = 35
start_time = time.time()
result = fibonacci_recursive(n)
end_time = time.time()

print(f"Result: {result}")
print(f"Runtime: {end_time - start_time} seconds")

# Profiling Runtime across multiple runs

for n in range(10, 42, 5):
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    print(f"Runtime for fibonacci_recursive({n}): {end_time - start_time} seconds")

# start = time.time()
# fibonacci_recursive(43)
# end = time.time()
# print(f"Elapsed time for n=43: {end - start:.2f} seconds")
#
# start = time.time()
# fibonacci_iterative(100_000)
# end = time.time()
# print(f"Elapsed time: {end - start:.2f} seconds")
