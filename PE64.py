from euler import *

def is_square(n):
    return int(np.sqrt(n))**2 == n

def get_sequence(n):
    rt = np.sqrt(n)
    a0 = int(rt)
    a = int(rt)
    d = 1
    m = 0

    cnt = 0

    while True:
        cnt += 1
        m = int(d*a-m)
        d = int((n-m*m)/d)
        a = int((rt+m)/d)

        if a == 2*a0:
            return cnt

@timer
def main():
    tot = 0
    maxx = 10000
    for i in range(2, maxx+1):
        if is_square(i):
            continue
        lenn = get_sequence(i)
        if lenn%2 == 1:
            tot += 1
    print(tot)


if __name__ == "__main__":
    main()
