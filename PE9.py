from math import *

def is_square(c):
    rt = sqrt(c)
    return int(rt) == rt, int(rt)

def get_triplets(n):
    ts = []
    for a in range(2, n):
        for b in range(2, n):
            if a+b > n:
                continue
            c2 = a*a+b*b
            is_sqr, c = is_square(c2)
            if is_sqr:
                ts.append([a, b, c])
    return ts

ts = get_triplets(1000)
for t in ts:
    if t[0]+t[1]+t[2] == 1000:
        print(t[0]*t[1]*t[2])
