from euler import *

def is_harshad(n):
    d_sum = digit_sum(n)
    d, m = divmod(n, d_sum)
    return  m == 0

def is_strong_harshad(n):
    d_sum = digit_sum(n)
    d, m = divmod(n, d_sum)
    return  m == 0 and is_prime(d)

def add_if_strong(n):
    out = 0
    if is_strong_harshad(n):
        for j in [1, 3, 7, 9]:
             p = n*10+j
             if p >= 100 and is_prime(p):
                 out += p
    return out

def solve(n):
    n_digits = n
    cur_harshads = [i for i in range(1, 10)]

    total = 0

    for i in range(n_digits-1):
        next_harshads = []

        for h in cur_harshads:
            total += add_if_strong(h)
            next_base = h*10

            for j in range(10):
                next = next_base+j

                if is_harshad(next):
                    next_harshads.append(next)

            cur_harshads = next_harshads

    return total

@timer
def main():
    t = solve(14)
    print(t)


if __name__ == "__main__":
    #print(is_strong_harshad(18))
    main()
