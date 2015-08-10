__author__ = 'alex'
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5 #first 6k - 1
    while i * i <= n: #since primes are only before sqrt(n)
        if n % i == 0 or n % (i + 2) == 0: #i + 2 = 6k + 1
            return False
        i += 6

    return True

print is_prime(7)