# f(n) = f(n-1) + f(n-2


def find_fib(n):
    if n<=1:
        return n

    fib1 = find_fib(n-1)
    fib2 = find_fib(n-2)
    return fib1 + fib2

print(find_fib(6))