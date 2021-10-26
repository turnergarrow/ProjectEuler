from euler import *
from scipy import stats


def A_l(n):
    beta = np.pi-np.arctan(n)

    alpha = np.arcsin(np.sin(beta)*(1-1./n))

    phi = np.pi-beta-alpha

    A_arc = phi/8.

    s = (np.sin(phi))/(2*np.sin(beta))

    A_c = s*np.sin(alpha)/4

    A_b = A_arc-A_c
    A_t = 1/(8.*n)

    return A_t-A_b

def A_tot():
    return (4.-np.pi)/16

def ratio(n):
    return A_l(n)/A_tot()

@timer
def main():
    r = 1
    n = 0
    while r > 0.001:
        n += 1
        r = ratio(n)
    print(r, n)

if __name__ == "__main__":
    main()
