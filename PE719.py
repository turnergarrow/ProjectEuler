from euler import *

# NOT a fast solution, takes longer than the time limit
# Finds a solution eventually

n = int(1e6)

def is_S(m, n):

    if (m < n) or n <= 0: return False
    if (m == n): return True

    t = 10
    while (t < m):
        div, mod = divmod(m, t)
        if is_S(div, n-mod):
            return True
        t = t*10

    return False


if __name__ == "__main__":
    tot = 0
    for i in range(2, n+1):
        sqr = i*i
        if is_S(sqr, i):
            print(i, sqr)
            tot += sqr
    print(tot)
