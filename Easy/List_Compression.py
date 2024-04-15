x = int(input())
y = int(input())
z = int(input())
n = int(input())
probability = []
for x in range(x+1):
    for y in range(y+1):
        for z in range(z+1):
            probability.append([x, y, z])

sum = []
for i in probability:
    if (i[0]+i[1]+i[2]) != n:
        sum.append(i)
print(sum)
