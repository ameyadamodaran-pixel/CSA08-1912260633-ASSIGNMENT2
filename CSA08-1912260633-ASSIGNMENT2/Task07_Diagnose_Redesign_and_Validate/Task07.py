# Q7 - Diagnose, Redesign and Validate
# Selected limitation: repeated recursive work in Q6.

from functools import lru_cache
import time

calls = 0
def original_recursive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return original_recursive(n - 1) + original_recursive(n - 2)

def redesigned_iterative(n):
    """O(n) time and O(1) auxiliary space."""
    if n <= 1:
        return 1
    previous, current = 1, 1
    iterations = 0
    for _ in range(2, n + 1):
        previous, current = current, previous + current
        iterations += 1
    return current, iterations

def time_call(function, n):
    start = time.perf_counter()
    result = function(n)
    return result, time.perf_counter() - start

print("Original vs redesigned solution")
for n in (20, 25, 30):
    calls = 0
    old_value, old_time = time_call(original_recursive, n)
    old_calls = calls
    (new_value, iterations), new_time = time_call(redesigned_iterative, n)
    print(f"n={n}: same_result={old_value == new_value}, "
          f"original_calls={old_calls}, new_iterations={iterations}, "
          f"original_time={old_time:.6f}s, redesigned_time={new_time:.6f}s")

print("\nDiagnosis: naive recursion recalculates the same smaller step counts.")
print("Objective: preserve the result while reducing work to a linear number of iterations.")
print("Trade-off: the loop uses two stored values and avoids recursive stack growth.")
