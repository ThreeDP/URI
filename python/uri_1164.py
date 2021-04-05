n = int(input())

for i in range(n):
    number = int(input())
    j = 1
    perfect = 0
    while j < number:
        if number % j == 0:
            perfect += j
        j += 1

    if perfect == number:
        print("{} eh perfeito".format(number))
    else:
        print("{} nao eh perfeito".format(number))
