from euler import *

@jit
def all_odd(n):
    while n > 0:
        n, m = divmod(n, 10)
        if m%2 == 0:
            return False
    return True

@timer
@jit
def main():
    maxx = int(1e9)
    tot = 0
    for i in range(0, maxx+1):
        r = reverse(i)
        summ = i+r
        if r>0 and all_odd(summ):
            tot += 1
    print(tot)

if __name__ == "__main__":
    main()
