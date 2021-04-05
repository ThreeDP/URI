a, b, c = [float(x) for x in input().split(" ")]

try:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Impossivel calcular")
    else:
        x1 = (- b + delta ** 0.5) / (2 * a)
        x2 = (- b - delta ** 0.5) / (2 * a)
        print("R1 = {:.5f}\nR2 = {:.5f}".format(x1, x2))
except:
    print("Impossivel calcular")

