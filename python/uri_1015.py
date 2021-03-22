p1 = [float(x) for x in input().split(" ")]
p2 = [float(y) for y in input().split(" ")]

distance = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
print("{:.4f}".format(distance))
