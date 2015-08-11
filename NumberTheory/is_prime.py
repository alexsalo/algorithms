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

def eratosthenes_sieve(n):
    numbers = [i for i in range(2, n)]
    pi = 0 # index
    while pi < len(numbers):
        p = numbers[pi] # current prime
        i = 2 # start with closet multiple
        while p * i <= n: # while multiple less than N -> remove it from the list (if it is still in)
            if numbers.__contains__(p * i):
                numbers.remove(p * i)
            i += 1
        pi += 1
    return numbers

def eratosthenes_sieve_refine(n):
    numbers = [i for i in range(2, n)]
    pi = 0
    while True:
        p = numbers[pi]
        p_sq = p ** 2
        if p_sq > n:
            break
        while p_sq <= n:
            if numbers.__contains__(p_sq):
                numbers.remove(p_sq)
            p_sq += p
        pi += 1
    return numbers

import math
def eratosthenes_sieve_bool(n):
    prime_bool = (n + 1) * [True] # since indexing starts with 0
    for p in range(2, int(math.sqrt(n)) + 1): #int floors the float
        if prime_bool[p]:
            for i in range(p ** 2, n + 1, p): # p^2, p^2 + p, p^2 + 2p ...
                prime_bool[i] = False
    return [i for i, elem in enumerate(prime_bool) if elem][2:]

def eratosthenes_sieve_bool_odd(n):
    prime_bool = [True, True, True] + (n / 2 - 1)  * [True, False]
    for p in range(2, int(math.sqrt(n)) + 1): #int floors the float
        if prime_bool[p]:
            for i in range(p ** 2, n, 2 * p):
                prime_bool[i] = False
    return [i for i, elem in enumerate(prime_bool) if elem][2:]

print is_prime(49)
print eratosthenes_sieve(200)
print eratosthenes_sieve_refine(200)
print eratosthenes_sieve_bool(200)
print eratosthenes_sieve_bool_odd(200)

import time

s = time.time()
eratosthenes_sieve(2000)
print 'eratosthenes_sieve exec time: ' + str(time.time() - s)

s = time.time()
eratosthenes_sieve(2000)
print 'eratosthenes_sieve refine exec time: ' + str(time.time() - s)

s = time.time()
eratosthenes_sieve_bool(2000)
print 'eratosthenes_sieve bool exec time: ' + str(time.time() - s)

s = time.time()
eratosthenes_sieve_bool_odd(2000)
print 'eratosthenes_sieve bool odd time: ' + str(time.time() - s)