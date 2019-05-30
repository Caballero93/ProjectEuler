"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    """
    Checks if number num is palindrome. Returns True if it is, or False if it is not.
    """
    # convert number to string
    num_str = str(num)
    # reverse version of the number
    num_reverse = num_str[::-1]

    # if number and its reversed version are the same, the number is palindrome
    return num_str == num_reverse

##### Solution
# Nested for loop starting from the biggest 3-digit number is used. If product of two loop counters is 
# palindrome number that number is remembered and inner loop is stopped, because another palindrome with # # same outer loop counter and smaller inner loop conter gives smaller result for sure.

biggest_palindrome = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if is_palindrome(product):
            if product > biggest_palindrome:
                biggest_palindrome = product
            break

print("The biggest palindrom which is product of two 3-digit numbers is: {}" \
        .format(biggest_palindrome))

