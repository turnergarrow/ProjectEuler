import numpy as np
import math as m
import copy as cp
from datetime import datetime as dt
import time
from numba import jit
import random as rand
from scipy import special
import cProfile
import pstats

def timer(f):
    def wrapper(*args):
        start = time.time()
        f(*args)
        end = time.time()
        print(f"Took {end-start} s")
    return wrapper

# get the number of factors of a number
@jit
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
@jit
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
    return fac

# get prime factors of a number
@jit
def get_primes(n):
    primes = []
    r = 0

    for i in range(2, m.ceil(m.sqrt(n))+1):
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
@jit
def sieve(n):
    n = int(n)
    prime = [False, True]*(n//2)
    prime[1], prime[2] = False, True
    if n%2 == 1:
        prime.append(True)

    p = 3
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
@jit
def is_prime(n):
    if n == 2:
        return True
    for i in range(2, m.ceil(m.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# check if number is prime
@jit
def digit_sum(n):
    if n < 0:
        return -1
    if n < 10:
        return n
    summ = 0
    while n > 0:
        n, m = divmod(n, 10)
        summ += m
    return summ

@jit
def reverse(n):
    r = 0
    d, m = divmod(n, 10)
    if m == 0:
        return -1
    while n > 0:
        r *= 10
        n, m = divmod(n, 10)
        r += m
    return r

def is_palindrome(n):
    return n == reverse(n)

def is_int(n):
    return np.isclose(n, int(n))
