age = []
i = 1
while i > 0:
    age.append(int(input()))
    i = age[-1]
average = sum(age[:-1]) / (len(age) - 1)
print("{:.2f}".format(average))