import time

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

start = time.perf_counter_ns()

summ = 0
gen = fib()
num = next(gen)
while num <= 4000000:
    if not num % 2:
        summ += num
    num = next(gen)

end = time.perf_counter_ns()
print("Time elapsed:", end - start, "ns")

print("Result =", summ)
