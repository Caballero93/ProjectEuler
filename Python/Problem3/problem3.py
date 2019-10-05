"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
###
# Every whole number can be written as the product of its prime factors. Problem can be solved recursively,
# by finding smallest prime factor of the number and dividing the starting number with the returned prime factor. Problem is solved when the smallest prime factor of the number is the number itself.

def is_prime(num):
    """
    Returns True if number is prime, false otherwise.
    """
    # 2 and 3 are prime numbers
    if num in [2, 3]:
        return True
    # if number is not in form of 6n-1 or 6n+1 - it is not prime number
    elif not num % 6 in [1, 5]:
        return False
    else:
        # find if number has divisors
        for i in range(2, num // 2 + 1):
            if not num % i:
                return False
        return True

def smallest_prime_factor(num):
    """
    Finds the smallest prime factor of the number.
    """
    # if number is divisor of num and it is prime number - return it
    for i in range(2, num // 2 + 1):
        if not num % i and is_prime(i):
            return i
    # if divisor is not found - return num
    return num


def biggest_prime_factor(num):
    """
    Finds the biggest prime factor of the number.
    """
    smallest_prime_fac = smallest_prime_factor(num) 
    if smallest_prime_fac == num:
        return num
    else:
        return biggest_prime_factor(num // smallest_prime_fac)

print("Biggest prime factor of 13195: {}".format(biggest_prime_factor(13195)))
print("Biggest prime factor of 600851475143: {}".format(biggest_prime_factor(600851475143)))