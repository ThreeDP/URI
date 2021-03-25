N = int(input())
for n in range(N):
    p1 = (n + 1) * (n + 1)
    p2 = (n + 1) * p1
    print("{} {} {}".format((n + 1), p1, p2))