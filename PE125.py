from euler import *

@timer
def main():
    n_start = 1
    maxx = 1e8
    pals = []
    while n_start**2 < maxx:
        sqr_sum = n_start**2
        i = n_start
        while sqr_sum < maxx:
            i += 1
            sqr_sum += i**2
            if is_palindrome(sqr_sum) and sqr_sum < maxx and sqr_sum not in pals:
                pals.append(sqr_sum)

        n_start += 1
    print(sum(pals))


if __name__ == "__main__":
    main()
