#Challenge: Optimize the function to handle large input numbers efficiently.
#=====================================================
#Description: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False otherwise.
...
import math

def is_prime(number):
    if number <=1:
        return False
    if number <= 3:
        return True
    if number %2 == 0 and number % 3 == 0:
        return False

    for i in range (5, int(math.isqrt(number)) + 1, 6):
        if number % i == 0 or number % (i+2) == 0:
            return False

    return True
print(is_prime(2))
print(is_prime(29))
print(is_prime (100))