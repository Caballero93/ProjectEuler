def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

summ = 0
for num in fib(4000000):
    if not num % 2:
        summ += num

print(summ)
