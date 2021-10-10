a = 1504170715041707
b = 4503599627370517

coins = [1504170715041707]

n = 1

while coins[-1] > 1:
    calc = a*n%b
    if n%1000000 == 0:
        print(n)
    if calc < coins[-1]:
        print(coins)
        coins.append(calc)
    n += 1

print(sum(coins))
