while True:
    x = float(input())
    if x < 0 or x > 10:
        print("nota invalida")
        continue
    break
while True:
    y = float(input())
    if y < 0 or y > 10:
        print("nota invalida")
        continue
    break
result = (x + y) / 2
print("media = {:.2f}".format(result))