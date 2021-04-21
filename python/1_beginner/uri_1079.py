
for i in range(0, int(input()), 1):
    result = 0
    n1, n2, n3 = [float(x) for x in input().split(" ")]
    result = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    print("{:.1f}".format(result))
