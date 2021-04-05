fuel = {1: 0, 2: 0, 3: 0}
n = 0
while n != 4:
    n = int(input())
    if n >= 1 and n <= 3:
        fuel[n] += 1
    else:
        continue

print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(fuel[1], fuel[2], fuel[3]))