numbers = [int(x) for x in input().split()]
cres = [int(y) for y in numbers]
cres.sort()

for number in cres:
    print(number)

print()
for number in numbers:
    print(number)