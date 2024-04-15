details = []
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    details.append([name, grade])
print(details)

gradet = []
for i in range(len(details)):
    gradet.append(details[i][1])
print(gradet)
gradesort = gradet.sort(reverse=True)
print(gradesort)
# slowest = gradesort[-2]
# print(slowest)

# name = []
# for i in range(len(gradesort)):
#     if slowest == details[i][1]:
#         name.append(details[i][0])
#     print(name)
