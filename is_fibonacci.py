import math
""""Function to check for compliance of each line with the Fibonacci sequence"""

def is_fibonacci(n):
    if type(n) not in [int]:
       raise TypeError("Type must be int only")
    if n < 0:
        raise ValueError("Number of fibonacci can't be negative")
    a = (0.5 + 0.5 * math.sqrt(5.0)) * n
    return n == 0 or abs(round(a) - a) < 1.0 / n