def get_n_factors(num):
    tot = 0
    i = 1
    while i*i < num:
        if num%i == 0:
            tot += 2
        i += 1
    if i*i == num:
        tot += 1
    return tot

i = 1
to_add = 2

while(True):
    n = get_n_factors(i)
    if n > 500:
        break
    i = i + to_add
    to_add += 1

print(i)
