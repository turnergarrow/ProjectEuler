import itertools
from euler import *

lines = [(0, 5, 6), (1, 6, 7), (2, 7, 8), (3, 8, 9), (4, 9, 5)]

def is_valid_perm(p):
    c1 = p[0] == 10 or p[1] == 10 or p[2] == 10 or p[3] == 10 or p[4] == 10
    c2 = p[0] < p[1] and p[0] < p[2] and p[0] < p[3] and p[0] < p[4]
    return c1 and c2

def get_string(p):
    tot = 0
    for l in lines:
        for i in l:
            factor = p[i]
            tot *= 10 if p[i] != 10 else 100
            tot += p[i]
    return tot

@timer
def main():
    best = 0
    for p in itertools.permutations(list(range(1, 11))):
        if not is_valid_perm(p):
            continue
        l = lines[0]
        summ = p[l[0]]+p[l[1]]+p[l[2]]
        broke = False
        for l in lines[1:]:
            sum2 = p[l[0]]+p[l[1]]+p[l[2]]
            if sum2 != summ:
                broke = True
                break
        if not broke:
            str_p = get_string(p)
            best = max(best, str_p)
    print(best)




if __name__ == "__main__":
    main()
