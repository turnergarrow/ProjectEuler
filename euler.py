import numpy as np
import math as m
import copy as cp
from datetime import datetime as dt
import time
from numba import jit
import random as rand
from scipy import special

def timer(f):
    def wrapper():
        start = time.time()
        f()
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
    for i in range(2, m.ceil(m.sqrt(n))):
        if n%i == 0:
            return False
    return True
