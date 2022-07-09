import time

from functools import cache


N: int = 400

# def cache(fnc):
#     history = {}
#     def wrapper(n):
#         if n not in history:
#             history[n] = fnc(n)
#         return history[n]
#     return wrapper

#@cache
def fib_recursion(n: int) -> int:
    return 1 if n < 2 else fib_recursion(n - 1) + fib_recursion(n - 2)

fib_recursion_start_time: float = time.time()
fib_recursion_results: int = fib_recursion(N)
fib_recursion_end_time: float = time.time()
print(fib_recursion_results)
print(f"Rekurencyjnie zajeło: {fib_recursion_end_time - fib_recursion_start_time}")

# z cache 0.0010085105895996094