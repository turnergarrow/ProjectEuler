import numpy as np
import math as m
import copy as cp

# get the number of factors of a number
def get_n_factors(num):
    tot = 0
    i = 1
    while i*i < num:
        if num%i == 0:
            tot += 2
        i += 1
    if i*i == num:
        tot += 1
    return tot

# get the factors of a number
def get_factors(num):
    fac = []
    i = 1
    while i*i < num:
        if num%i == 0:
            fac.append(i)
            fac.append(int(num/i))
        i += 1
    if i*i == num:
        fac.append(i)
    return tot

# get prime factors of a number
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

# get all prime numbers up to n
def sieve(n):
    prime = list(True for i in range(n))

    p = 2
    while p*p <= n:
        if prime[p]:
            p_mult = 2*p
            while(p_mult < n):
                prime[p_mult] = False
                p_mult += p
        p += 1

    ps = []
    for i in range(2, n):
        if prime[i]:
            ps.append(i)
    return ps

# check if number is prime
def is_prime(n):
    for i in range(2, ceil(sqrt(n))):
        if n%i == 0:
            return False
    return True
