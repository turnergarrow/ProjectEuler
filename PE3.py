from math import *

def is_prime(n):
    for i in range(2, ceil(sqrt(n))):
        if n%i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    r = 0

    for i in range(2, ceil(sqrt(n))+1):
        if n%i == 0:
            primes.append(i)
            r = int(n/i)
            break
    if r == 0:
        return [n]
    else:
        primes = primes + get_primes(r)
        return primes

print(max(get_primes(600851475143)))
