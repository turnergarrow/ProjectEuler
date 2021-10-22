from euler import *
from scipy import stats

@timer
def main():
    print(7*stats.hypergeom.sf(0, 70, 10, 20))

if __name__ == "__main__":
    main()
