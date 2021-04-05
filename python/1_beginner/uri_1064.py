sum = 0
positive = 0
for value in range(6):
    number = float(input())
    if number > 0:
        sum += number
        positive += 1

print("{} valores positivos\n{:.1f}".format(positive, (sum / positive)))