from euler import *

def r_max(a):
    if a % 2 == 0:
        return (a-2)*a
    else:
        return (a-1)*a

@timer
def main():
    a = 7
    tot = 0
    for a in range(3, 1001):
        tot += r_max(a)
    print(tot)


if __name__ == "__main__":
    main()
