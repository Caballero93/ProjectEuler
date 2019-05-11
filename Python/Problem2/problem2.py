def create_fibonacci(n):
    """
    Creates list of fibonacci numbers up to number n.
    """
    fib = [1, 2]
    while (fib[-1] + fib[-2]) < n:
        fib.append(fib[-1] + fib[-2])

    return fib

# create list of fibonacci numbers up to 4000000
fib = create_fibonacci(4000000)
# get sum of even numbers from this list
sum_even = sum(i if not i % 2 else 0 for i in fib)
print(sum_even)