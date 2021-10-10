from math import *

maxx = 50000000

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

p = sieve(ceil(sqrt(maxx)))

twos = []
threes = []
fours = []

nums = []

i = 0
while True:
    if i == len(p): break
    val = p[i]**2
    if val > maxx:
        break
    twos.append(val)
    i += 1

i = 0
while True:
    val = p[i]**3
    if val > maxx:
        break
    threes.append(val)
    i += 1

i = 0
while True:
    val = p[i]**4
    if val > maxx:
        break
    fours.append(val)
    i += 1

print(twos, threes, fours)

for i in twos:
    for j in threes:
        for k in fours:
            nums.append(i+j+k)

out = set(filter(lambda x: x < maxx, nums))
print(len(out))
