x = int(input())
n = 0
while n < 6:
    if x % 2 != 0:
        print(x)
        x += 1
        n += 1
    else:
        x += 1

