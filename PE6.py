def sum_n(n):
    return n*(n+1)/2

def sum_square(n):
    tot = 0
    for i in range(1, n+1):
        tot += i*i
    return tot

def square_sum(n):
    return sum_n(n)**2

def diff(n):
    return square_sum(n)-sum_square(n)

print(diff(100))
