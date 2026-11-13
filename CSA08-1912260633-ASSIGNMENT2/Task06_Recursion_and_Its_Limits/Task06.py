# Q6 - Recursion and Its Limits
from functools import lru_cache
import sys
import time

naive_calls = 0
def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

memo_calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_loop(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

if __name__ == "__main__":
    print("Correctness for n=1..6")
    for n in range(1, 7):
        print(n, ways_loop(n))

    print("\nCall-count growth")
    for n in (10, 20, 25, 30):
        naive_calls = 0
        naive_value = ways_naive(n)
        memo_calls = 0
        ways_memo.cache_clear()
        memo_value = ways_memo(n)
        print(f"n={n}: value={naive_value}, naive_calls={naive_calls}, "
              f"memo_value={memo_value}, memo_calls={memo_calls}")

    print("\nIterative result for n=1000 has", len(str(ways_loop(1000))), "digits")
    try:
        ways_memo.cache_clear()
        memo_calls = 0
        ways_memo(1000)
    except RecursionError as error:
        print("Memoised recursion at n=1000:", type(error).__name__)
        print("Recursion limit:", sys.getrecursionlimit())
        print("Reason: memoisation avoids repeated work, but recursive calls still use stack frames.")
