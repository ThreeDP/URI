x = int(input())
y = int(input())

if y < x:
    z = x
    x = y
    y = z

x += 1
while x < y:
    if (x % 5 == 2) or (x % 5 == 3):
        print(x)
    x += 1