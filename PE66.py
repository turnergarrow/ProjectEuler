from euler import *


def is_solved(x, y, D):
    return x*x-D*y*y == 1

def get_cont_frac(n):
    mn = 0.0
    dn = 1.0
    a0 = int(np.sqrt(n))
    an = int(np.sqrt(n))
    convergents = [a0]

    if a0 != np.sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            convergents.append(an)
    return convergents[:-1]

def get_x(D):
    sqrt_D = int(np.sqrt(D))
    m = 0
    d = 1
    a = sqrt_D

    h = a
    k = 1

    h1 = 1
    k1 = 0

    while not is_solved(h, k, D):
        m = int(d*a-m)
        d = int((D-m*m)/d)
        a = int((sqrt_D+m)/d)

        h2 = h1
        k2 = k1

        h1 = h
        k1 = k

        h = a*h1 + h2
        k = a*k1 + k2

    return h


@timer
def main():
    n = 1000
    maxx = 0
    D = 0
    for i in range(2, n+1):
        sqrt_i = np.sqrt(i)
        if int(sqrt_i) == sqrt_i:
            continue
        x = get_x(i)
        if x > maxx:
            maxx = x
            D = i
    print(D)

if __name__ == "__main__":
    main()
