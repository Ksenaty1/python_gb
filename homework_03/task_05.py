def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


ls = [fib(i) * (-1) ** (i + 1) for i in range(1, 10)]
print(ls)