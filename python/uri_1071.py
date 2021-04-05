x = int(input())
y = int(input())
i = x
sum = 0

while x > y:
    if x % 2 != 0 and x != i:
        sum += x
    x -= 1
print(sum)
