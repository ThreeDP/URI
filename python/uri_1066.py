even = 0
odd = 0
positive = 0
negative = 0
for n in range(5):
    n = float(input())
    if int(n % 2) == 0:
        even += 1
    else:
        odd += 1
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1

print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(even, odd, positive, negative))
