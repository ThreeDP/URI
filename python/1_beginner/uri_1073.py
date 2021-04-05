n = int(input())
x = 1
while x <= n:
    if x % 2 == 0:
        print("{}^2 = {}".format(x, x ** 2))
        x += 1
    else:
        x += 1

