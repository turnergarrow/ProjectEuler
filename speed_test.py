from euler import *

@timer
def main():
    for i in range(int(1e5)):
        get_n_factors(i)

if __name__ == "__main__":
    main()
