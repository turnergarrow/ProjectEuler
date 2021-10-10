num = [1]

for i in range(1000):
    rng = len(num) if num[0] < 5 else len(num)+1
    j = 0
    while j < rng:
    # for j in range(rng):
        n = num[j]
        new = 2*n
        num[j] = new%10
        if new>=10:
            if j == 0:
                num.insert(0, 1)
                j+=1
            else:
                num[j-1] += 1
        j += 1

print(sum(num))
