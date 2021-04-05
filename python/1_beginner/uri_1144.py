N = int(input())
p1 = 0
p2 = 0

i = N - 1
while i >= 0:
    p1 = (N - i) * (N - i)
    p2 = (N - i) * p1
    print(N - i, p1, p2)
    print(N - i, p1 + 1, p2 +1)
    i -= 1






