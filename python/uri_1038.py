product = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

X, Y = [int(x) for x in input().split(" ")]
total = product[X] * Y

print("Total: R$ {:.2f}".format(total))