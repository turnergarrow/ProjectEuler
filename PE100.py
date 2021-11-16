from euler import *

@timer
def main():
    n_0 = 1
    d_0 = 1
    while d_0 <= 1e12:
        n_1 = 3*n_0 + 2*d_0 - 2
        d_1 = 4*n_0 + 3*d_0 - 3

        n_0 = n_1
        d_0 = d_1

    print(n_0)



if __name__ == "__main__":
    main()
