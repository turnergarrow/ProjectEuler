def a_sums_to_b(a, b):
    a_str = str(a)
    tot = 0
    for i in a_str:
        tot += int(i)
    return tot == b

def fib(n):
    f0 = 0
    f1 = 1
    fn = 0
    for i in range(n):
        fn = f0+f1
        f0 = f1
        f1 = fn
    return f0

def s(n):
    i = 1
    while True:
        if a_sums_to_b(i, n):
            return i
        i += 1

def S(k):
    tot = 0
    for n in range(1, k+1):
        tot += s(n)
    return tot

def f(maxx):
    tot = 0
    for i in range(2, maxx):
        print(i)
        tot += S(fib(i))
    return tot

print(f(20))
