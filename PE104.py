from euler import *

def contains_all(n):
    if n < 1e8:
        return False
    contains = np.zeros(10)
    while n > 0:
        n, r = divmod(n, 10)
        if contains[r] or r == 0:
            return False
        else:
            contains[r] = 1
    return True

@timer
def main():
    i = 2

    first_0 = 1
    first_1 = 1

    last_0 = 1
    last_1 = 1

    e9 = int(1e9)

    while True:
        _, summ = divmod(last_1+last_0, e9)
        last_0 = last_1
        last_1 = summ

        s = first_0+first_1
        first_0 = first_1
        first_1 = s
        if first_1 >= int(1e15):
            first_0 //= 10
            first_1 //= 10

        i += 1
        if contains_all(first_1//1000000) and contains_all(last_1):
            break
    print(i)

if __name__ == "__main__":
    main()
