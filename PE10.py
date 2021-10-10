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

ps = sieve(2000000)
print(sum(ps))
