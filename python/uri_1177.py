t = int(input())
n = []
p = 0
i = 0

while i < (1000):
    n.append(p)
    print("N[{}] = {}".format(i, p))

    if p < (t-1):
        p += 1
    else:
        p = 0
    i += 1
