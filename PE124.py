from euler import *

def rad(n):
    for i in range(2, m.ceil(np.sqrt(n))+1):
        while n % i**2 == 0:
            n = n//i
    return n


@timer
def main():
    n_start = 1
    maxx = 100000
    inds = np.zeros(maxx+1)
    rads = np.zeros(maxx+1)
    for i in range(1, maxx+1):
        rads[i] = i
        inds[i] = rad(i)
    srted = [x for _, x in sorted(zip(inds, rads))]
    print(int(srted[10000]))


if __name__ == "__main__":
    main()
