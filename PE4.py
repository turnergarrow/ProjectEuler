from math import *

def is_pal(n):
    n_str = str(n)
    for i in range(ceil(len(n_str)/2)):
        if n_str[i] != n_str[-i-1]:
            return False
    return True

n_max = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        p = i*j
        if p > n_max and is_pal(p):
            n_max = p

print(n_max)
