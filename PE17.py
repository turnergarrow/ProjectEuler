ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [6, 6, 5, 5, 5, 7, 6, 6]

hundred = 7

for t in tens:
    for j in range(0, 10):
        ones.append(t+ones[j])

for h in range(1, 10):
    for o in ones[0:100]:
        andd = 0 if o==0 else 3
        val = ones[h]+hundred+andd+o
        ones.append(val)

thou = 3+8

print(sum(ones)+thou)
