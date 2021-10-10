from math import *

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

all_primes = [0 for i in range(0, 21)]

for i in range(2, 21):
    ps = get_primes(i)
    prime_list = list(0 for j in range(0, i+1))
    for p in ps:
        prime_list[p] += 1
    for p in range(len(prime_list)):
        if all_primes[p] < prime_list[p]:
            all_primes[p] = prime_list[p]

tot = 1
for i in range(len(all_primes)):
    for j in range(all_primes[i]):
        tot *= i

print(tot)
