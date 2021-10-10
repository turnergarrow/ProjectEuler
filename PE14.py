def collatz(n):
    d, m = divmod(n, 2)
    if m == 0:
        return d
    return 3*n+1

def len_chain(n):
    lenn = 1
    if cache[n]:
        print('cached')
        return cache[n]
    while n != 1:
        n = collatz(n)
        lenn += 1
    return lenn

cache = [0 for i in range(1000000)]

print(len_chain(13))

maxx = 0
n = 0
for i in range(1, 1000000):
    chain = len_chain(i)
    cache[i] = chain
    if chain > maxx:
        print(i, chain)
        maxx = chain
        n = i

print(n)
print(cache[0:20])
